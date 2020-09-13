# MIDI-python-assignment
Programming exercise transposing a public domain song in C-major to C-minor in code

## Author
Chase E. Stewart

## Contents
This file contains the following folders and files:
* `./MIDIConstants.py` - a class file with some of the required variables to do the 
* `./transpose.py` - the skeleton file where you will write your code to transpose the input file to match the output reference
* `./reference/Nannerl_allegro_in_C.mid` - A public-domain MIDI file that serves as our input file
* `./reference/Reference_Allegro_Cm_output.mid` - A reference MIDI output file I've created using my solution 
* `./README.md` - this file
* `.gitignore` - here and in `output/.gitignore`, these files keep certain other files from being added to Git version control.
This is useful to keep PyCharm project files and intermediate/solution MIDI files out of the repo.
A good general rule is not to include static non-code files that can easily be re-generated using the code in the Repo.

## Requirements
* This assignment is designed for Python3 and the MIDO python package
* You will first need to `pip install` the [Mido Python Package](https://mido.readthedocs.io/en/latest/intro.html) to get this to work.
* You can use Windows Media Player or something like `https://onlinesequencer.net/import` to play your created files online.

## Usage
just run `python transpose.py <path/to/file.mid>`. If left blank, the program will default to operating on the default 
public-domain MIDI file in the repository.

## References
* For understanding the MIDO python package, there's the official [Mido Package Documentation](https://mido.readthedocs.io/en/latest/intro.html)
* Information for sufficient understanding of [writing MIDI through software is Here](https://www.cs.cmu.edu/~music/cmsip/readings/MIDI%20tutorial%20for%20programmers.html)
* [This music stackexchange answer](https://music.stackexchange.com/questions/88027/transposing-from-c-to-cm) helped me devise 
the method to transpose the song from C to Cm
