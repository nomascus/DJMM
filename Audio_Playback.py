#!/usr/bin/env python3
import sys
import pysynth as ps
from pydub import AudioSegment
from pydub.playback import play
import re

#Script for taking the musical notes and playing them back as audio for project DJMM Prog4Bio 2018

#Using pysynth to make the wav file
#Note names have to be a to g
#sharps = #, flats = b
#format is (note, duration) with 4 as a quarter note, x is a whole note


#Make all lowercase

#Take the music notes generated from the song

#keynotes = sys.argv[1]

#Cat mtDNA:
#keynotes = ['B2', 'E4', 'G4', 'G#', 'D', 'G2', 'D#', 'G4', 'D3', 'G#2', 'C3', 'D2', 'F', 'B', 'D#3', 'G4', 'C3', 'E3', 'D#4', 'C#', 'C#', 'D3', 'C#', 'B2', 'B', 'C', 'G#', 'F2', 'C#3', 'E2', 'F#', ' ', 'G4', 'G#', 'F#3', 'C2', 'F#', 'F#4', 'E4', 'F#2', 'G', 'D4', 'C#3', 'F', 'F2', 'A#2', ' ', 'C#3', 'F#', 'E4', 'F2', 'B2', 'D#3', 'F#', 'G#2', 'C', 'G#2', 'E2', 'F#2', 'G2', 'B', ' ', 'D3', 'G2', 'F#', 'G4', 'D#3', 'G#2', 'B2', 'C3', 'D4', 'E3', 'F3', 'C#2', 'E4', 'E3', 'C#2', 'C4', 'C2', 'G#2', 'C2', 'E', ' 2', 'C', 'G#', 'C4', 'D#3', 'F2', 'D#4', 'C4', 'G#2', 'F', 'G#2', 'C', 'G#2', 'C4', 'D#4', 'C4', 'G#2', 'C#4', 'G#2', 'C', 'G#2', 'C4', 'D#4', 'C4', 'G#2', 'C#4', 'G#2', 'C', 'G#2', 'C4', 'D#4', 'C4', 'G#2', 'C#4', 'G#2', 'C', 'G#2', 'C4', 'D#4', 'C4', 'G#2', 'C#4', 'G#2', 'C', 'G#2', 'C4', 'D#4', 'C4', 'G#2', 'C#4', 'G#2', 'C', 'G#2', 'C4', 'D#4', 'C4', 'G#2']

#Tale as old as time:
#keynotes = ['G','Bb','D','D#','G#', ' ', 'G', 'Bb', 'D', 'D#', 'F', ' ', 'D#', 'F', 'G', 'G#', 'Bb', ' ', 'Bb', 'G#', 'G', 'F', 'D#', ' ', 'G#', 'G', 'F', 'D#', 'Bb', ' ',]

#Test:
#keynotes = ['G4', ' 2', 'C3', ' ', 'G2', 'C2', 'E', 'C#', 'C#4']

#Let it go:
#keynotes = let_it_go = ['A', 'B', 'C', ' ', 'G', 'G', 'D', ' ', 'C', 'A2', 'A2', 'A2', 'A', 'B', 'C', ' ', 'A', 'B', 'C', ' ', 'G', 'E', 'E', 'D', ' ', 'C', 'D2', 'E2', 'E2', 'F2', 'E2', 'D2', 'C2', 'D2', 'C2', ' ', 'G', 'E', 'D', ' ', 'C2', 'C2', 'G', 'E', 'C', ' ', 'C', 'C', 'B', 'G', 'G']

#Sound of music do re mi:
#keynotes = ['C', 'D2', 'E', ' ', 'C', 'E2', 'C2', 'E', ' ', 'D', 'E2', 'F', ' ', 'F', 'E2', 'D2', 'F', ' ', 'E', 'F2', 'G', ' ' , 'E2', 'G', 'E2', 'G', ' ', 'F', 'G2', 'A2', 'A', 'G', 'F', 'A']

#The hobbit
keynotes = ['C2', 'D2', 'E', 'G', 'E2', 'D2', 'C', ' ', 'E2', 'G2', 'A', 'C4', 'B2', 'G2', 'E2', 'F4', 'E3', 'D2', ' ', 'C2', 'D2', 'E', 'G', 'E2', 'D2', 'C', ' ', 'E2', 'G2', 'A', 'F2' 'E2', 'F2', 'E2', 'D2', 'C1']



test = []

for note in keynotes:
	note = note.lower()
	if " 2" == note:
		value = ['r',4]
		test.append(value)

	elif "2" in note:
		note_letter = re.search(r"([A-Za-z]+#?)\d?", note)
		value = [note_letter.group(1),4]
		#print("Found a 2")
		test.append(value)
#print(note)
#print(value)
#print(test)
#Stay positive
	elif "4" in note:
		note_letter = re.search(r"([A-Za-z]+#?)\d?", note)
		value = [note_letter.group(1)+"5",4]
		test.append(value)
			
#print(test)
	elif "3" in note:
		note_letter = re.search(r"([A-Za-z]+#?)\d?", note)
		value = [note_letter.group(1)+"5",2]
		test.append(value)
		
#print(test)
	elif " " in note:
		value = ['r',2]
		test.append(value)
		
	else:
		note_letter = re.search(r"([A-Za-z]+#?)\d?", note)
		value = [note_letter.group(1),2]
		test.append(value)

#test = (('c', 4), ('e', 4), ('g', 4),
#		('c5', -2), ('e6', 8), ('d#6', 2))

ps.make_wav(test, fn = "test_real.wav", bpm = 360)

#Using Pydub to play the wav file generated
sound_file = "test_real.wav"
sound = AudioSegment.from_file(sound_file, format="wav")
play(sound)
