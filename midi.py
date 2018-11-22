from midiutil.MidiFile import MIDIFile
import music21

# create your MIDI object


# C,G,Am,F
chordprog1 = []
chordprog1 =  [ ('c3','e3','g3') , ('g3','b3','d3') , ('ab3','c3','eb3') , ('f3','a3','c3') ]
# Am   G     F     G 
chordprog2 = [ ('ab3','c3','eb3'), ('g3','b3','d3'),  ('f3','a3','c3'), ('g3','b3','d3')]

def convertToMIDI( melodyTuple , chords, tempo, filename):


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
        for i in chordprog1:
            print("this is the", i[0], "note at time:", time)
            volume=70
            duration = 4
            for x in i:
                pitch = music21.pitch.Pitch(x).midi
                mf.addNote(1, channel, pitch, time, duration, volume)
            time = time+ duration
        

    with open(filename + ".mid", 'wb') as outf:
        mf.writeFile(outf)