import random
import pysynth_p
import pysynth_e
import pysynth_c
import os
import constants
import collections
from hsl import analyzePartitions
from pydub import AudioSegment
from fitness import down_beat_fitness, monotonic_notes_fitness, octave_range_fitness, back_beat_fitness, down_beat_fitness, isSignificantNote, no_jump_fitness


def gen_population(pop_size, dna_size):
    return [ gen_dna(dna_size) for _ in range (pop_size) ]

def gen_dna(dna_size):
    return [ gen_chromosone() for _ in range (dna_size) ]

# what is a chromosome?
# chromosomes  within genomes consist of a tuple(?) containing a diatonic letter index, octave identifier, and an 
# absolute note value.

# Diatonic letter - index representing one of "c d e f g a b" aka the major scale and "r" for rest
# Octave identifier - represents one of five octaves from C2 to C7
# absolute note value - product of octave index*amount of notes per octave+diatonic letter index
# Ex. C2 is represented as (0,0,0), B2 is (6,0,6), middle C is (0,2,16) and a rest can be (7,3,31)

def gen_chromosone():
    octave_idx = random.choice(constants.OCTAVE_IDX)
    note_idx = random.choice(constants.NOTE_IDX)

    # which octave * size of octave  + note in that octave
    abs_note = octave_idx * constants.NUM_DIATONIC_REST + note_idx
    duration = constants.DEFAULT_DURATION
    return (note_idx, octave_idx, abs_note, duration)

def fitness_prop_selection(population_with_score_sorted):
    sum_scores = sum([score for score, dna in population_with_score_sorted])
    population_with_proportion_sorted = [
            (score / float(sum_scores), dna) for score, dna in
                population_with_score_sorted ]


    last_sum_prop = 0
    population_sum_prop_sorted= []
    for prop, dna in population_with_proportion_sorted:
        last_sum_prop += prop
        population_sum_prop_sorted.append((last_sum_prop, dna))

    r = random.uniform(0,1)

    for sum_prop, dan in population_sum_prop_sorted:
        if (r < sum_prop):
            # print sum_prop
            return dna

    raise Exception('We should not get here')

def crossover(first_parent, second_parent):
    len_dna = len(first_parent)
    crossover_idx = random.randrange(0, len_dna)

    first_child = first_parent[0:crossover_idx] + second_parent[crossover_idx:]
    second_child = second_parent[0:crossover_idx] + first_parent[crossover_idx:]
    return first_child, second_child

def mutate_dna(dna):
    def mutate_chromosone(chromosone):
        r = random.randint(0,100)

        if r <= constants.MUTATION_PERCENTAGE:
            return gen_chromosone()
        else:
            return chromosone

    return [ mutate_chromosone(chromosone) for chromosone in dna]
#Returns scored populations SORTED
def score_population(population):
    population_with_score = []
    for dna in population:
        score = 0
        score += 3*octave_range_fitness(dna)
        score += 2*monotonic_notes_fitness(dna)
        score += 2*no_jump_fitness(dna)
        score += down_beat_fitness(dna)
        score += back_beat_fitness(dna)

        population_with_score.append((score, dna))

    #Ascending
    population_with_score_sorted = sorted(
            population_with_score, key=lambda t: t[0])

    return population_with_score_sorted

def run_iteration(population):
    population_with_score_sorted = score_population(population)
    new_pop = []
    while (len(new_pop) < constants.POPULATION):
        first_parent = fitness_prop_selection(population_with_score_sorted)
        second_parent = fitness_prop_selection(population_with_score_sorted)
        first_child, second_child = crossover(first_parent, second_parent)
        new_pop.append(first_child)
        new_pop.append(second_child)

    mutated_population = [
            mutate_dna(dna) for dna in new_pop]

    return mutated_population

def run_genetic_algo():
    population = gen_population(constants.POPULATION, constants.BEATS_PER_SECTION)

    for _ in range(constants.ITERATIONS):
        population = run_iteration(population)

    return score_population(population)[0][1]

def massage(section):
    new_section = []
    skip = False
    for i in range(0, len(section) - 1):
        if skip:
            skip = False
            continue
        c_note = section[i][0]
        n_note = section[i+1][0]
        c_duration = section[i][1]
        if c_note == n_note:
            # print(c_note, n_note)
            dur = 2 if c_duration > 2 else 1
            new_section.append((c_note, dur))
            skip = True
        else:
            new_section.append((c_note,c_duration))

    return tuple(new_section)

def arrange_song_into_aaba(a,b):
    return a+a+b+a

def generateBeat():
    dur = constants.DEFAULT_DURATION
    beat = []
    for chromosone in range(int(constants.BEATS_PER_SECTION*4)):
        if (chromosone%4 == 0):
            beat.append(('c',2))
            beat.append(('f',2))
        # else:
        #     beat.append(('f',dur/2))
    return  tuple(beat)

def generateBasslineSection(note):

    bass=[]
    for chromosone in range(int(constants.BEATS_PER_SECTION/2)):
       bass.append((note,64))
    return  tuple(bass)

def generateBassline(notes,len):
    bass =[]
    for note in notes:
        bass.extend(generateBasslineSection(note))
        print(note)
    print('actual',bass)
    return bass*len



def combineWAVs(a,b,c):

    sound1 = AudioSegment.from_file(a)
    sound2 = AudioSegment.from_file(b)

    combined = sound1.overlay(sound2) 

    combined.export(c, format='wav')

def changeScale(scale):
    if (scale == 1):
        constants.DIATONIC = constants.MAJOR_NOTES
        print("GOTEMzz")
    elif(scale == 2):
        constants.DIATONIC = constants.MINOR_NOTES
        print("GOTEMs")
    # else:
    #     constants.DIATONIC = constants.ALL_NOTES
    #     print("GOTEM")

def changeOctaves(min,max):
    constants.MIN_OCTAVE = int(min)
    constants.MAX_OCTAVE = int(max)
    constants.OCTAVES = range(constants.MIN_OCTAVE, constants.MAX_OCTAVE + 1)
    constants.NUM_OCTAVES = len(constants.OCTAVES)
    constants.OCTAVE_IDX = range(constants.NUM_OCTAVES)
    constants.NUM_NOTES  = constants.NUM_OCTAVES * constants.NUM_DIATONIC_REST





    
