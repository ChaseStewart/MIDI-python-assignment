#!/usr/bin/python

from MIDIConstants import *
from mido import *

"""
Fill in the commented sections below with code to complete the project 
"""

# first open the input MidiFile by calling MidiFile("path/to/file.mid")
#    store it in a variable, like `mid = MidiFile("path.mid")`

# Now print the MidiFile's `type` and `ticks_per_beat`

# Create a new empty output MidiFile with a different variable name
#    NOTE: When you create the new MidiFile, be sure to set its `type` and `ticks_per_beat` to match the input MidiFile

# Create a new empty MidiTrack just the same as you created a MidiFile and store it in a variable

# `Append` the new MidiTrack to the MidiFile

# Create a new variable with all the input messages using `merge_tracks(MidiFile.tracks)`

# Now loop over all `messages` in `merge_tracks`

# For every message in merge_tracks: if the message `is_meta`, copy it to the new MidiFile.MidiTrack

# else if the message is one of MIDIConstants.py's MIDI_MSG_NOTES types, do the following:
#    If the note is one of the values `in` C_MAJ_TRANSPOSE_IN, convert it into the equivalent within C_MIN_TRANSPOSE_OUT
#       HINT: LIST.index will be helpful here, and prepare to use square-bracket indexing.
#       After converting the note, just `Append` it to your new track

#    Else if the note is a MIDI_MSG_NOTES type and is not `in` C_MAJ_TRANSPOSE, then just `Append` the msg as-is

# Finally, now that we've looped over every message in the input midi file and either copied or transposed every message
# call `new_midi_file.save()`, giving the output file a proper name. Be sure to put the output in the `output/` folder

# When this is done, open the file using some kind of MIDI music player

# Listen to the output sound and compare it to the `Reference_allegro_Cm_output.mid