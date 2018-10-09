from genetic_algorithm import run_genetic_algo, massage,generateBassline,generateBeat,combineWAVs, arrange_song_into_aaba
from mapping import mapValues
from misc import dnaToPsSong
from constants import BPM
import random
import pysynth_p
import pysynth_e
import pysynth_c
import os
import collections
from hsl import analyzePartitions
from pydub import AudioSegment

if __name__ == "__main__":

    ## First gets input from user, will later accept by the mapping modules output
    filename = input("What image?")
    color_value = []
    print("Analyzing image...")
    color_values = analyzePartitions(filename)
    mapValues(color_values)

    print("Running genetic algorithms...")
# GENETIC ALGORITHM PART
    a = run_genetic_algo()
    b = run_genetic_algo()
    dna = arrange_song_into_aaba(a,b) 

#CONVERTING TO PySynth
    tune = dnaToPsSong(dna)
    massaged_tune = massage(tune)

    print("Generating beat...")
    beat = massage(generateBeat())
    progressions = [['c','d','g','eb'], ['c','d','g','eb'],['c','d','g','eb']]
    notes = ['c','d','g','eb']
    print("Generating bassline...")
    bass = massage(generateBassline(notes))
    # print('bass',bass)
    # print('beat',beat)
    # print('tune', tune)
    # print(massaged_tune)

    rest_lists = [ ('r',4) ]
    tune_plus_rest = tuple(list(massaged_tune) + rest_lists)

    # pysynth_c.make_wav(massaged_tune, fn = "output.wav", leg_stac = .7, bpm = bpm)
    print("Making WAVs...")
    pysynth_e.make_wav(tune_plus_rest, fn = "output_melody.wav",  bpm = BPM)
    pysynth_p.make_wav(beat, fn = "output_beat.wav",  bpm = BPM)
    pysynth_c.make_wav(bass, fn = "output_bass.wav",  bpm = BPM)

    # print(MIN_OCTAVE);
    # print(MAX_OCTAVE);


    print("Combining audio layers...")
    combineWAVs("output_melody.wav","output_beat.wav","output_final.wav")
    combineWAVs("output_final.wav","output_bass.wav","output_final.wav")

    print(len(tune))
    print(len(beat))
    print(len(bass))

    # Works for Linux
    # os.system('xdg-open "output_final.wav"')
    # os.system('xdg-open "'+ filename + '.png"')