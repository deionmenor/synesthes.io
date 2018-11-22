from genetic_algorithm import run_genetic_algo, massage,generateBassline,generateBeat, combineWAVs, arrange_song_into_aaba
from mapping import mapValues
from misc import dnaToPsSong
import constants
import random
import pysynth_p
import pysynth_e
import pysynth_d
import os
import collections
from hsl import analyzePartitions
from pydub import AudioSegment
from midi import convertToMIDI

if __name__ == "__main__":

    ## First gets input from user, will later accept by the mapping modules output
    filename = input("What image?")
    runs = input("How many tries?")
    color_value = []
    print("Analyzing image...")
    color_values = analyzePartitions(filename)
    mapValues(color_values)

    print("Running genetic algorithms...")

    for i in range(int(runs)):
    # GENETIC ALGORITHM PART
        a = run_genetic_algo()
        b = run_genetic_algo()
        dna = arrange_song_into_aaba(a,b) 

    

    #CONVERTING TO PySynth
        section_a = massage(dnaToPsSong(a))
        section_b = massage(dnaToPsSong(b))
        tune = dnaToPsSong(dna)
        massaged_tune = massage(tune)
        print(massaged_tune)
        

        print("Generating beat...")
        beat = massage(generateBeat())
        progressions = [['c','d','g','eb'], ['c','d','g','eb'],['c','d','g','eb']]
        notes = ['c','d','g','eb']
        print("Generating bassline...")
        bass = massage(generateBassline(notes,8))
        print(bass, "THIS THE BASS")
        intro = massage(generateBassline(notes,1))

        print("tempo is:", constants.BPM)
        filename = "output_"+str(i)
        convertToMIDI(massaged_tune, bass, constants.BPM, filename )

        # rest_lists = [ ('r',4) ]
        tune_plus_rest = tuple(list(massaged_tune))

        # pysynth_c.make_wav(massaged_tune, fn = "output.wav", leg_stac = .7, bpm = bpm)
        print("Making WAVs...")
        # pysynth_e.make_wav(tune_plus_rest, fn = "output_melody.wav",  bpm = constants.BPM)
        # pysynth_p.make_wav(beat, fn = "output_beat.wav",  bpm = constants.BPM)
        # pysynth_d.make_wav(bass, fn = "output_bass.wav",  bpm = constants.BPM)
        # pysynth_d.make_wav(intro, fn = "output_intro.wav",  bpm = constants.BPM)



        # pysynth_e.make_wav(section_a, fn = "output_melody_section_a.wav",  bpm = constants.BPM)
        # pysynth_e.make_wav(section_b, fn = "output_melody_section_b.wav",  bpm = constants.BPM)

        #make bass lower

        # bass_file = AudioSegment.from_wav("output_bass.wav")
        # bass_ = bass_file[:]
        # bass_ = bass_ - 20
        # bass_.export("output_bass.wav", format="wav")

        # bass_file = AudioSegment.from_wav("output_intro.wav")
        # bass_ = bass_file[:]
        # bass_ = bass_ - 20
        # bass_.export("output_intro.wav", format="wav")

        print("Combining audio layers...")
        # combineWAVs("output_melody.wav","output_beat.wav","output_final.wav")
        # combineWAVs("output_final.wav","output_bass.wav",filename + "/output_final_" + str(i) +".wav")

        print(len(tune))
        print(len(beat))
        print(len(bass))

        print("min octave: ", constants.MIN_OCTAVE)
        print("notes", constants.DIATONIC)
        print("BPM", constants.BPM)
        print("beats per section", constants.BEATS_PER_SECTION)

    # Works for Linux
    # os.system('xdg-open "' + filename + '/output_final_0.wav"')
    # os.system('xdg-open "'+ filename + '.png"')