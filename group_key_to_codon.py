#!/usr/bin/env python3
import random

tale_as_old_as_time = ['G','Bb','D','D#','G#', ' ', 'G', 'Bb', 'D', 'D#', 'F', ' ', 'D#', 'F', 'G', 'G#', 'Bb', ' ', 'Bb', 'G#', 'G', 'F', 'D#', ' ', 'G#', 'G', 'F', 'D#', 'Bb', ' ',]

let_it_go = ['A', 'B', 'C', ' ', 'G', 'G', 'D', ' ', 'C', 'A2', 'A2', 'A2', 'A', 'B', 'C', ' ', 'A', 'B', 'C', ' ', 'G', 'E', 'E', 'D', ' ', 'C', 'D2', 'E2', 'E2', 'F2', 'E2', 'D2', 'C2', 'D2', 'C2', ' ', 'G', 'E', 'D', ' ', 'C2', 'C2', 'G', 'E', 'C', ' ', 'C', 'C', 'B', 'G', 'G']

do_re_mi = ['C', 'D2', 'E', ' ', 'C', 'E2', 'C2', 'E', ' ', 'D', 'E2', 'F', ' ', 'F', 'E2', 'D2', 'F', ' ', 'E', 'F2', 'G', ' ' , 'E2', 'G', 'E2', 'G', ' ', 'F', 'G2', 'A2', 'A', 'G', 'F', 'A']

### keys are assigned a numeric value. the '2' version of each key is designated as the half note
key_dict = {'C':'1', 'C2':'2', 'C#':'3', 'Db':'3', 'C#2':'4', 'Db2':'4', 'D':'5', 'D2':'6', 'D#':'7', 'Eb':'7', 'D#2':'8', 'Eb2':'8', 'E':'9', 'E2': '10', 'F':'11', 'F2':'12', 'F#':'13', 'Gb':'13', 'F#2':'14', 'Gb2':'14', 'G':'15', 'G2':'16', 'G#':'17', 'Ab':'17', 'G#2':'18', 'Ab2':'18', 'A':'19', 'A2':'20', 'A#':'21', 'Bb':'21', 'A#2':'22', 'Bb2':'22', 'B':'23', 'B2':'24', 'C3':'25', 'C4':'26', 'C#3':'27', 'Db3':'27', 'C#4':'28', 'Db4':'28', 'D3':'29', 'D4':'30', 'D#3':'31', 'Eb3':'31', 'D#4':'32', 'Eb4':'32', 'E3':'33', 'E4':'34', 'F3':'35', 'F4':'36', 'F#3':'37', 'Gb3':'37', 'F#4':'38', 'Gb4':'38', 'G3':'39', 'G4':'40', ' ':'41', ' 2':'42'}

#print(key_dict)

### this dictionary was picked randomly
#key_to_codon_dict = {'1':['F1'], '2':['F2'], '3':['L1', 'L2', 'L3'], '4':['L4', 'L5', 'L6'], '5':['I1', 'I2'], '6':['I3'], '7':['V1', 'V2'], '8':['V3', 'V4'], '9':['S1', 'S2', 'S3'], '10':['S4', 'S5', 'S6'], '11':['P1', 'P2'], '12':['P3','P4'], '13':['M'], '14':['M'], '15':['T1','T2'], '16':['T3', 'T4'], '17':['G1', 'G2'], '18':['G3', 'G4'], '19':['Y1'], '20':['Y2'], '21':['H1'], '22':['H2'], '23':['Q1'], '24':['Q2'], '25':['N1'], '26':['N2'], '27':['K1'], '28':['K2'], '29':['D1'], '30':['D2'], '31':['E1'], '32':['E2'], '33':['C1'], '34':['C2'], '35':['R1', 'R2', 'R3'], '36':['R4', 'R5', 'R6'], '37':['Z1', 'Z2'], '38':['Z3'], '39':['W'], '40':['W'], '41':['A1', 'A2'], '42':['A3','A4']}


### this dictionary accounts for amino acid frequency. Most frequent AA is on the white keys. http://www.tiem.utk.edu/~gross/bioed/webmodules/aminoacid.htm
key_to_codon_dict = {'1':['R1', 'R2', 'R3'], '2':['R4', 'R5', 'R6'], '3':['F1'], '4':['F2'], '5':['N1'], '6':['N2'], '7':['P1', 'P2'], '8':['P3', 'P4'], '9':['D1'], '10':['D2'], '11':['C1'], '12':['C2'], '13':['S1', 'S2', 'S3'], '14':['S4', 'S5', 'S6'], '15':['Q1'], '16':['Q2'], '17':['T1', 'T2'], '18':['T3', 'T4'], '19':['E1'], '20':['E2'], '21':['W'], '22':['W'], '23':['G1', 'G2'], '24':['G3', 'G4'], '25':['H1'], '26':['H2'], '27':['Y1'], '28':['Y2'], '29':['I1', 'I2'], '30':['I3'], '31':['V1', 'V2'], '32':['V3', 'V4'], '33':['L1', 'L2', 'L3'], '34':['L4', 'L5', 'L6'], '35':['K1'], '36':['K2'], '37':['Z1', 'Z2'], '38':['Z3'], '39':['M'], '40':['M'], '41':['A1', 'A2'], '42':['A3', 'A4']}

### empty dictionary
#key_to_codon_dict = {'1':[''], '2':[''], '3':[''], '4':[''], '5':[''], '6':[''], '7':[''], '8':[''], '9':[''], '10':[''], '11':[''], '12':[''], '13':[''], '14':[''], '15':[''], '16':[''], '17':[''], '18':[''], '19':[''], '20':[''], '21':[''], '22':[''], '23':[''], '24':[''], '25':[''], '26':[''], '27':[''], '28':[''], '29':[''], '30':[''], '31':[''], '32':[''], '33':[''], '34':[''], '35':[''], '36':[''], '37':[''], '38':[''], '39':[''], '40':[''], '41':[''], '42':['']}



###stop codon was assigned Z
codon_to_nt_dict = {'F1':'TTT', 'F2':'TTC', 'L1':'TTA', 'L2':'TTG', 'L3':'CTT', 'L4':'CTC', 'L5':'CTA', 'L6':'CTG', 'I1':'ATT', 'I2':'ATC', 'I3': 'ATA', 'M': 'ATG', 'V1': 'GTT', 'V2':'GTC', 'V3':'GTA', 'V4':'GTG', 'S1':'TCT', 'S2':'TCC', 'S3':'TCA', 'S4':'TCG', 'S5':'AGT', 'S6':'AGC', 'P1':'CCT', 'P2':'CCC', 'P3':'CCA', 'P4':'CCG', 'T1':'ACT', 'T2':'ACC', 'T3':'ACA', 'T4':'ACG', 'A1':'GCT', 'A2':'GCC', 'A3':'GCA', 'A4':'GCG', 'Y1':'TAT', 'Y2': 'TAC', 'Z1':'TAA', 'Z2':'TAG', 'Z3':'TGA', 'H1':'CAT', 'H2':'CAC', 'Q1':'CAA', 'Q2':'CAG', 'N1':'AAT', 'N2':'AAC', 'K1':'AAA', 'K2':'AAG', 'D1':'GAT', 'D2':'GAC', 'E1':'GAA', 'E2':'GAG', 'C1':'TGT', 'C2':'TGC', 'W':'TGG', 'R1':'CGT', 'R2':'CGC', 'R3':'CGA', 'R4':'CGG', 'R5':'AGA', 'R6':'AGG', 'G1':'GGT', 'G2':'GGC', 'G3':'GGA', 'G4':'GGG'}

#print(codon_to_nt_dict)

###this is used to convert a song input into nucleotide sequence
numbers =[]
note_to_codons = []
for note in do_re_mi:
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
print(note_to_codons)

sequence = ''
for aa in note_to_codons:
    nt = codon_to_nt_dict[aa]
    sequence+=nt

print(sequence)

