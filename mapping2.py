from genetic_algorithm import changeOctaves,changeScale
import constants

def mapValuesSequentially(HSL):
    # scale = input("scale? (1) major (2) minor (3) mixed ---> ")
    # scale = 1
    # lightness_values_sum = 0
    # for i in HSL:
    #     lightness_values_sum+= i[2]
    # lightness_average = lightness_values_sum/9
    # print("ave L: ",lightness_average)


    # saturation_values_sum = 0
    # for i in HSL:
    #     saturation_values_sum+= i[1]
    # saturation_average = saturation_values_sum/9
    # print("ave S: ", saturation_average)

    # hue_values_sum = 0
    # for i in HSL:
    #     hue_values_sum+= i[1]
    # hue_average = hue_values_sum/9
    # print("ave H: ",hue_average)
 
    # variance = 0
    # # get how much variance in hue
    # for i in HSL:
    #     variance += abs(i[1]-hue_average)
    # variance = variance/9
    # print("ave V: ",variance)

    mino = getOctave(HSL[2])
    print(mino)
    maxo = mino+1
    # BPM = int(input("BPM ---> "))
    constants.BPM = getBPM(HSL[1])
    changeOctaves(mino,maxo)
    changeScale(1)


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