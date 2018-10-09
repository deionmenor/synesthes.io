from genetic_algorithm import changeOctaves,changeScale

def mapValues(HSL):
    global BPM
    # scale = input("scale? (1) major (2) minor (3) mixed ---> ")
    scale = 1
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
    print(mino)
    maxo = mino
    # BPM = int(input("BPM ---> "))
    BPM = getBPM(saturation_average)
    changeOctaves(mino,maxo)
    changeScale(scale)


def getBPM(ave):
    ave = ave * 100
    if ave < 20:
        return 80
    elif ave < 60:
        return 120
    else:
        return 180


def getOctave(ave):
    ave = ave * 100
    if ave < 17:
        return 2
    elif ave < 33:
        return 3
    elif ave < 50:
        return 4
    elif ave < 67:
        return 5
    elif ave < 84:
        return 6
    else:
        return 7