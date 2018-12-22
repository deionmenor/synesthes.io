from genetic_algorithm import changeOctaves,changeScale
import constants
import random
import music21

#https://www.michael-thomas.com/music/class/chords_notesinchords.htm
#https://www.pianochord.org/bm7.html
#https://www.8notes.com/piano_chord_chart/cdim7.asp
#CHORD PROGRESSIONS
ACTIVE_WARM = [[('c','e','g'), ('a','c','e'), ('d','f','a'), ('e','g#','b','d')],[('c','e','g'), ('d','f','a'), ('e','g','b'), ('f','a','c')], [('c','e','g'), ('e', 'g#', 'b', 'd'), ('a','c','e'), ('c','e','g','bb')], [('c', 'e', 'g'), ('b', 'd', 'f#', 'a'), ('e','g#','b','d'), ('a','c','e')]]

ACTIVE_COOL = [[('c','e','g'), ('c', 'e', 'g#'), ('c','e','g','a'), ('c', 'e', 'g#')], [('c','e','g'), ('c', 'e', 'g', 'b'), ('c', 'e', 'g','bb')], [('c', 'e', 'g'), ('e','g','b'), ('e','g','b','d')]]

PASSIVE_WARM = [[('c','e','g'), ('g', 'bb', 'd'), ('c', 'e', 'g','bb'), ('f','a','c')], [('c','e','g'), ('g','b','d'), ('a','c','e'), ('e','g','b')], [('c','e','g'), ('e','g','b'), ('f','a','c'), ('g','b','d')], [('c','e','g'), ('a','c','e'), ('d','f','a','c'), ('g','b','d')], [('c','e','g'), ('bb', 'd', 'f'), ('f','a','c'), ('c','e','g')], [('c','e','g'),('f','a','c'),('g','b','d'),('c','e','g')], [('c','e','g'), ('d','f','a','c'), ('g','b','d','f'), ('c','e','g')]] 

PASSIVE_COOL = [[('c','e','g'), ('c','d#','f#','a'), ('d','f','a','c'),('g','b','d','f')], [('c','e','g'),('a','c','e'),('f','ab','c'),('g','b','d','f')], [('d','f#','a'),('g','b','d'),('f','a','c'),('a','c','e','g')]]


def mapValues(HSL):
    lightness_values_sum = 0
    for i in HSL:
        lightness_values_sum+= i[2]
    lightness_average = lightness_values_sum/9
    print("ave L: ",lightness_average)


    saturation_values_sum = 0
    for i in HSL:
        saturation_values_sum+= i[1]
    saturation_average = saturation_values_sum/9
    print("ave S: ", saturation_average)

    hue_values_sum = 0
    for i in HSL:
        hue_values_sum+= i[1]
    hue_average = hue_values_sum/9
    print("ave H: ",hue_average)
 
    variance = 0
    # get how much variance in hue
    for i in HSL:
        variance += abs(i[1]-hue_average)
    variance = variance/9
    print("ave V: ",variance)

    mino = getOctave(lightness_average)
    maxo = mino+1
    bpm = getBPM(saturation_average)
    chord_prog = getProgression(hue_average, saturation_average)

    
    return (mino,maxo,bpm,chord_prog)

    # changeOctaves(mino,maxo)
    # changeScale(scale)

    


def getBPM(ave):
    ave = ave * 100
    if ave < 20:
        return 100
    elif ave < 50:
        return 130
    else:
        return 150


def getOctave(ave):
    ave = ave * 100
    if ave < 25:
        return 3
    elif ave < 50:
        return 4
    elif ave < 75:
        return 5
    else:
        return 6

def getProgression(hue, saturation):
    print("hue:",hue,"sat:",saturation)
    if hue<= 359 and hue >= 271  and saturation >= 0.5:
        print("Mood for chord progression: active warm")
        return random.choice(ACTIVE_WARM)
    elif hue<= 89 and hue >= 0  and saturation >= 0.5:
        print("Mood for chord progression: active warm")
        return random.choice(ACTIVE_WARM)
    elif hue >= 90 and hue <= 270  and saturation >= 0.5:
        print("Mood for chord progression: active cool")
        return random.choice(ACTIVE_COOL)
    elif hue<= 359 and hue >= 271  and saturation >= 0.49:
        print("Mood for chord progression: passive warm")
        return random.choice(PASSIVE_WARM)
    elif hue<= 89 and hue >= 0 and saturation <= 0.49: 
        print("Mood for chord progression: passive warm")
        return random.choice(PASSIVE_WARM)
    elif hue >= 90 and hue <= 270 and saturation <= 0.49:
        print("Mood for chord progression: passive cool")
        return random.choice(PASSIVE_COOL)
    