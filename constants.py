BPM = 121
MIN_OCTAVE = 3
MAX_OCTAVE = 4
OCTAVES = range(MIN_OCTAVE, MAX_OCTAVE + 1)
NUM_OCTAVES = len(OCTAVES)
OCTAVE_IDX = range(NUM_OCTAVES)

#NOTES
MINOR_NOTES =  ['f','g','g#','a#','c','c#','eb']
MAJOR_NOTES =  ['c5','d5','e5','f5','g5','a5','b5']
# ALL_NOTES =  MAJOR_NOTES.extend(MINOR_NOTES)
DIATONIC = MINOR_NOTES
REST = ['r']
DIATONIC_REST = DIATONIC + REST
NUM_DIATONIC_REST = len(DIATONIC_REST)
NOTE_IDX = range(NUM_DIATONIC_REST)
NUM_NOTES  = NUM_OCTAVES * NUM_DIATONIC_REST

CHORD_PROGRESSION = [('c3','e3','g3') , ('g3','b3','d3') , ('ab3','c3','eb3') , ('f3','a3','c3')]


DEFAULT_DURATION = 8 # change back to 8
BARS_PER_SECTION = 4
BEATS_PER_BAR = 4
BEATS_PER_SECTION = BARS_PER_SECTION * BEATS_PER_BAR

TONIC = 'c'
CHORD_NOTES = 'ceg'


POPULATION = 50
assert POPULATION % 2 == 0
ITERATIONS = 200
MUTATION_PERCENTAGE = 2