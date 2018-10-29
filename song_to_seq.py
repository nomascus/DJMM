#!/usr/bin/env python3

#filename: 
#Owner:

#================
#Libaries
#===============





#============
#variables
#============




#=======================
#script
#======================


freq_to_letter_dict = {}
time_note = {}

import sys
import statistics
import subprocess
import random

#Pull in .wav file to aubio
filename = sys.argv[1]
aubio_output = subprocess.check_output('aubiopitch '+ filename, shell = True)
aubio_output = aubio_output.decode('utf-8')

#Split aubio list on newlines to make it readable
aubio_list = aubio_output.split("\n")

#Make a dictionary for duration and frequency of notes in music
freq_dict = {}
for line in aubio_list:
	line_split = line.split()
	if len(line_split) !=2:
		#print('Messed up',line)
		continue
	time = float(line_split[0])
	frequency = float(line_split[1])
	freq_dict[time] = frequency

#opening the reference musical-note-to-frequency file
with open('freq_note.txt','r') as file_obj2:
	for line in file_obj2:
                min_max_dict = {}		#Open a sub-dictionary for each note
                line = line.rstrip()
                line_split = line.split()
                note = line_split[0]
                frequency_min =float(line_split[1])	#Take the minimum frequency
                frequency_max = float(line_split[2])	#Take the maximum frequency
                min_max_dict["mini"]=frequency_min	#Append the max/min frequency into the dictionary as a sub-dictionary
                min_max_dict["maxi"]=frequency_max
                freq_to_letter_dict[note] = min_max_dict            #Makes a dictionary with form {note:{min,max}}

#Loop through the notes in the reference dictionary
for note in freq_to_letter_dict:
    for minimum in freq_to_letter_dict[note]:    
        mini = freq_to_letter_dict[note]["mini"]
        maxi = freq_to_letter_dict[note]["maxi"]
        for time in freq_dict:					   #For each duration, assign a note based on frequency
            if mini<=freq_dict[time] and freq_dict[time] < maxi:   #If frequency between min/max of a note, assign that note
                time_note[time] = note   			   #Make a new dictionary of form {duration:note}
        else:
            continue						   #If it doesn't match the frequency, look thru more notes

#Assigning variables for the duration into consideration
start = 0
start_time=0
end_time=0
start_note = ''
end_note = ''

el_listerino = []

#For each time in the sorted duration:note dictionary check if long or short
for time in sorted(time_note, key=float):
    start = time
    note = time_note[time]
    if start_time == 0:			#For the very first note in the song
        start_time = start		#Reset all variables to this baseline note
        start_note = note
        end_time = time
    else:    				#If not first note
        if note == start_note:		#but if same as the last note played
            end_time = time		#increase the end time
        else:         			#If it is a different note than last played
            tiny_list = []			#Make a list every time to create a list of lists later - to keep order
            tiny_list.append(float(end_time) - float(start_time))	#calculate the duration of a note (end-start)
            tiny_list.append(start_note)				#for each, create the [duration,note] list
            el_listerino.append(tiny_list)				#append [duration,note] list into the bigger one
            start_note = note			#Reset all variables 
            start_time = time
            end_time = time

duration_list = []			 
for duration in el_listerino:			#To calculate the median, we need to make another list
    duration_list.append(duration[0])

least = min(duration_list)			#Least and most were used to sanity check the median
most = max(duration_list)
middle = statistics.median(duration_list)


notes_list = []				#The final countdown
for line in el_listerino:
	note, extra  = line[1].split("_")	#In the ref, the notes have "_" appended. Split here into proper notation
	duration = line[0]			
	if duration > middle:			#If the duration is longer than the median, consider it a whole note
		if note.endswith("3"):
			note = note.replace("3","4")	#Change from reference notation into next script's notation
			notes_list.append(note)
		else:				#If the duration is shorter or equal to the median, consider half note
			note = note+"2"		#Change from reference notation into the next script's notation
			notes_list.append(note)
	else:
		notes_list.append(note)	#This is the same notation as the next script, so leave


final_notes_list = []				
for note in notes_list:
	if note == "R":				#Change rest into the next scipt's notation
		note = " "
		final_notes_list.append(note)
	elif note == "R2":			#Change long rest into the next script's notation
		note = " 2"
		final_notes_list.append(note)
	else:
		final_notes_list.append(note)	#If not a rest, leave it


### keys are assigned a numeric value. the '2' version of each key is designated as the half note
key_dict = {'C':'1', 'C2':'2', 'C#':'3', 'Db':'3', 'C#2':'4', 'Db2':'4', 'D':'5', 'D2':'6', 'D#':'7', 'Eb':'7', 'D#2':'8', 'Eb2':'8', 'E':'9', 'E2': '10', 'F':'11', 'F2':'12', 'F#':'13', 'Gb':'13', 'F#2':'14', 'Gb2':'14', 'G':'15', 'G2':'16', 'G#':'17', 'Ab':'17', 'G#2':'18', 'Ab2':'18', 'A':'19', 'A2':'20', 'A#':'21', 'Bb':'21', 'A#2':'22', 'Bb2':'22', 'B':'23', 'B2':'24', 'C3':'25', 'C4':'26', 'C#3':'27', 'Db3':'27', 'C#4':'28', 'Db4':'28', 'D3':'29', 'D4':'30', 'D#3':'31', 'Eb3':'31', 'D#4':'32', 'Eb4':'32', 'E3':'33', 'E4':'34', 'F3':'35', 'F4':'36', 'F#3':'37', 'Gb3':'37', 'F#4':'38', 'Gb4':'38', 'G3':'39', 'G4':'40', ' ':'41', ' 2':'42'}

### this dictionary accounts for amino acid frequency. Most frequent AA is on the white keys. http://www.tiem.utk.edu/~gross/bioed/webmodules/aminoacid.htm
key_to_codon_dict = {'1':['R1', 'R2', 'R3'], '2':['R4', 'R5', 'R6'], '3':['F1'], '4':['F2'], '5':['N1'], '6':['N2'], '7':['P1', 'P2'], '8':['P3', 'P4'], '9':['D1'], '10':['D2'], '11':['C1'], '12':['C2'], '13':['S1', 'S2', 'S3'], '14':['S4', 'S5', 'S6'], '15':['Q1'], '16':['Q2'], '17':['T1', 'T2'], '18':['T3', 'T4'], '19':['E1'], '20':['E2'], '21':['W'], '22':['W'], '23':['G1', 'G2'], '24':['G3', 'G4'], '25':['H1'], '26':['H2'], '27':['Y1'], '28':['Y2'], '29':['I1', 'I2'], '30':['I3'], '31':['V1', 'V2'], '32':['V3', 'V4'], '33':['L1', 'L2', 'L3'], '34':['L4', 'L5', 'L6'], '35':['K1'], '36':['K2'], '37':['Z1', 'Z2'], '38':['Z3'], '39':['M'], '40':['M'], '41':['A1', 'A2'], '42':['A3', 'A4']}

###stop codon was assigned Z
codon_to_nt_dict = {'F1':'TTT', 'F2':'TTC', 'L1':'TTA', 'L2':'TTG', 'L3':'CTT', 'L4':'CTC', 'L5':'CTA', 'L6':'CTG', 'I1':'ATT', 'I2':'ATC', 'I3': 'ATA', 'M': 'ATG', 'V1': 'GTT', 'V2':'GTC', 'V3':'GTA', 'V4':'GTG', 'S1':'TCT', 'S2':'TCC', 'S3':'TCA', 'S4':'TCG', 'S5':'AGT', 'S6':'AGC', 'P1':'CCT', 'P2':'CCC', 'P3':'CCA', 'P4':'CCG', 'T1':'ACT', 'T2':'ACC', 'T3':'ACA', 'T4':'ACG', 'A1':'GCT', 'A2':'GCC', 'A3':'GCA', 'A4':'GCG', 'Y1':'TAT', 'Y2': 'TAC', 'Z1':'TAA', 'Z2':'TAG', 'Z3':'TGA', 'H1':'CAT', 'H2':'CAC', 'Q1':'CAA', 'Q2':'CAG', 'N1':'AAT', 'N2':'AAC', 'K1':'AAA', 'K2':'AAG', 'D1':'GAT', 'D2':'GAC', 'E1':'GAA', 'E2':'GAG', 'C1':'TGT', 'C2':'TGC', 'W':'TGG', 'R1':'CGT', 'R2':'CGC', 'R3':'CGA', 'R4':'CGG', 'R5':'AGA', 'R6':'AGG', 'G1':'GGT', 'G2':'GGC', 'G3':'GGA', 'G4':'GGG'}

###this is used to convert a song input into nucleotide sequence
numbers =[]
note_to_codons = []
for note in final_notes_list:
    number = key_dict[note]
    numbers.append(number)

for num in numbers:
    codons = key_to_codon_dict[num]
    if len(codons) ==1:
        associated_codon = key_to_codon_dict[num][0]
        note_to_codons.append(associated_codon)
    elif len(codons) >1:
        random_number = int(random.randrange(0, len(codons)))
        associated_codon = key_to_codon_dict[num][random_number]
        note_to_codons.append(associated_codon)
#print(note_to_codons)

sequence = ''
for aa in note_to_codons:
    nt = codon_to_nt_dict[aa]
    sequence+=nt

print(sequence)

