#!/usr/bin/env python3
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

keynotes = ['G4', ' 2', 'C3', ' ', 'G2', 'C2', 'E', 'C#', 'C#4']

test = []

for note in keynotes:
	note = note.lower()
	if " 2" == note:
		value = ['r',2]
		test.append(value)

	elif "2" in note:
		note_letter = re.search(r"([A-Za-z]+#?)\d?", note)
		value = [note_letter.group(1),2]
		#print("Found a 2")
		test.append(value)
#print(note)
#print(value)
#print(test)
#Stay positive
	elif "4" in note:
		note_letter = re.search(r"([A-Za-z]+#?)\d?", note)
		value = [note_letter.group(1)+"5",2]
		test.append(value)
			
#print(test)
	elif "3" in note:
		note_letter = re.search(r"([A-Za-z]+#?)\d?", note)
		value = [note_letter.group(1)+"5",1]
		test.append(value)
		
#print(test)
	elif " " in note:
		value = ['r',1]
		test.append(value)
		
	else:
		note_letter = re.search(r"([A-Za-z]+#?)\d?", note)
		value = [note_letter.group(1),1]
		test.append(value)

#test = (('c', 4), ('e', 4), ('g', 4),
#		('c5', -2), ('e6', 8), ('d#6', 2))

ps.make_wav(test, fn = "test_real.wav", bpm = 360)

#Using Pydub to play the wav file generated
sound_file = "test_real.wav"
sound = AudioSegment.from_file(sound_file, format="wav")
play(sound)
