from genetic_algorithm import run_genetic_algo, massage,generateBassline,generateBeat, combineWAVs, arrange_song_into_aaba
from mapping import mapValues, changeOctaves
from mapping2 import mapValuesSequentially
from misc import dnaToPsSong
import constants
import random
import os
import collections
from hsl import analyzePartitions, create_HSL_image
from hsl2 import analyzePartitionsSequentially
from pydub import AudioSegment
from midi import convertToMIDI
from midi2audio import FluidSynth

if __name__ == "__main__":

    # First gets input from user, will later accept by the mapping modules output
    filename = input("What image?")
    process = input("(1) Total or (2) Sequential?")
    soundfont = input("Soundfont?")
    runs = 1

    if soundfont=="": soundfont = "Kawai Grand Piano"

    chord_progression = [('c','e','g'), ('a','c','e'), ('d','f','a'), ('e','g#','b','d')]
    BPM = 120

    # TOTAL IMAGE ALGORITHM
    if process == "1":


        print("Analyzing image...")
        color_values = analyzePartitions(filename)
        
        ### create png with partitions and respective HSL values
        create_HSL_image(color_values,"img/"+filename)


        mino,maxo,BPM,chord_progression = mapValues(color_values)
        changeOctaves(mino,maxo)

        print("Running genetic algorithms...")

        for i in range(int(runs)):
        
            # create two melodies using the genetic algorithm
            a = run_genetic_algo()
            b = run_genetic_algo()
            dna = arrange_song_into_aaba(a,b) 
        
            section_a = massage(dnaToPsSong(a))
            section_b = massage(dnaToPsSong(b))
            tune = dnaToPsSong(dna)
            massaged_tune = massage(tune)
            print(massaged_tune)

            

            print("Generating beat...")
            beat = massage(generateBeat())
            progressions = [['c','d','g','eb'], ['c','d','g','eb'],['c','d','g','eb']]
            chord_progression = ['c','d','g','eb']
            print("Generating bassline...")
            print("tempo is:", BPM)
            file = "output_"+str(i)
            convertToMIDI(massaged_tune, chord_progression, BPM, file )

            os.system('xdg-open "'+ filename + '.png"')
            os.system('fluidsynth -ni ' + "\"soundfont/"+soundfont+'.sf2\" ' + file +'.mid -o audio.driver=alsa' )
        

    elif process == "2":
        


        # make measures shorter
        constants.BEATS_PER_SECTION = 32

        print("Partitioning and Analyzing Image...")
        color_values = analyzePartitionsSequentially(filename)

        for i in range(3):
            print("mapping values for partition,",i)
            mapValuesSequentially(color_values[i])
            a = run_genetic_algo()

            tune = dnaToPsSong(a)
            massaged_tune = massage(tune)
            print(massaged_tune)
            # print("Generating beat...")
            # beat = massage(generateBeat())
            print("Generating chords...")
            file = filename +"_" +str(i)
            convertToMIDI(massaged_tune, chord_progression, BPM, file )
            print(constants.BEATS_PER_SECTION)
  

    # Works for Linux
            
    # os.system('xdg-open "'+ filename + '.png"')