from midiutil.MidiFile import MIDIFile
import music21

# create your MIDI object

def convertToMIDI( melodyTuple , chordprog, tempo, filename):


    # create your MIDI object
    mf = MIDIFile(2)   

    time = 0    # start at the beginning
    mf.addTrackName(0, time, "melody")
    mf.addTrackName(1, time, "bass")
    mf.addTempo(0, time, tempo)
    mf.addTempo(1, time, tempo)

    # add some notes
    channel = 0
    volume = 100


    for i in melodyTuple:
        track = 0
        if i[0] == 'r':
            duration = i[1]/4
            pitch = 0
            mf.addNote(track, channel, pitch, time, duration, 0)
        else:
            duration = i[1]/4
            pitch = music21.pitch.Pitch(i[0]).midi
            mf.addNote(track, channel, pitch, time, duration, volume)
        time = time+ duration

    finaltime = time
    time=0
# make the chords
    while time<finaltime:
        for i in chordprog:
            # print("this is the", i[0], "note at time:", time)
            volume=70
            duration = 4
            for x in i:
                pitch = music21.pitch.Pitch(x).midi
                mf.addNote(1, channel, pitch, time, duration, volume)
            time = time+ duration

    with open(filename + ".mid", 'wb') as outf:
        mf.writeFile(outf)
