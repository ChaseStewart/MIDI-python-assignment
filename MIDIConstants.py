#!/usr/bin/python

"""
Different types of MIDI files
"""
# please see https://mido.readthedocs.io/en/latest/midi_files.html
MIDIFILE_SINGLE = 0
MIDIFILE_SYNCHRONOUS = 1
MIDIFILE_ASYNCHRONOUS = 2

"""
Search the input MIDI file for 'note_on' and 'note_off' messages 
to do the conversion
"""
MIDI_MSG_START_NOTE = 'note_on'
MIDI_MSG_STOP_NOTE = 'note_off'
MIDI_MSG_NOTES = [MIDI_MSG_START_NOTE, MIDI_MSG_STOP_NOTE]

"""
MIDI file translation table- the first item in C_MAJ_TRANPSOSE_IN 
should be converted to the first item in C_MIN_TRANSPOSE_OUT, etc
"""
# this is the "input list" of notes to be transposed within the MIDI file
# To "translate" a song to minor Key, we want to replace the 3rd, 6th, and 7th keys in each octave
# essentially, we take {4, 9, 11} for Octave -1, and add (12 * Octave_N) to each of those to transpose octave "N"
C_MAJ_TRANSPOSE_IN = [4, 9,  # Octave -2
                      16, 21,  # Octave -1
                      28, 33,  # Octave 0
                      40, 45,  # Octave 1
                      52, 57,  # Octave 2
                      64, 69,  # Octave 3
                      76, 81,  # Octave 4
                      88, 93,  # Octave 5
                      100, 105,  # Octave 6
                      112, 117,  # Octave 7
                      124]  # Octave 8/ end of MIDI range

# This is the "output list" of replacements for the to-be-transposed notes above
# NOTE: the 0th item in this list corresponds to the 0th in the list above, 1st-is-to-1st, etc
C_MIN_TRANSPOSE_OUT = [3, 8,  # Octave -2
                       15, 20,  # Octave -1
                       27, 32,  # Octave 0
                       39, 44,  # Octave 1
                       51, 56,  # Octave 2
                       63, 68,  # Octave 3
                       75, 80,  # Octave 4
                       87, 92,  # Octave 5
                       99, 104,  # Octave 6
                       111, 116,  # Octave 7
                       123]  # Octave 8/ end of MIDI range

