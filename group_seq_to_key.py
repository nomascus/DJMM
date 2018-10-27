#!/usr/bin/env python3
import re

class NotDNAError(Exception):
    pass

###stop codon was assigned Z
nt_to_codon_dict = {'TTT':'F1', 'TTC':'F2', 'TTA':'L1', 'TTG':'L2', 'CTT':'L3', 'CTC':'L4', 'CTA':'L5', 'CTG':'L6', 'ATT':'I1', 'ATC':'I2', 'ATA':'I3', 'ATG':'M',  'GTT':'V1', 'GTC':'V2', 'GTA':'V3', 'GTG':'V4', 'TCT':'S1','TCC':'S2', 'TCA':'S3', 'TCG':'S4', 'AGT':'S5', 'AGC':'S6', 'CCT':'P1', 'CCC':'P2', 'CCA':'P3', 'CCG':'P4','ACT':'T1','ACC':'T2', 'ACA':'T3', 'ACG':'T4', 'GCT':'A1', 'GCC':'A2', 'GCA':'A3', 'GCG':'A4', 'TAT':'Y1', 'TAC':'Y2', 'TAA':'Z1', 'TAG':'Z2', 'TGA':'Z3', 'CAT':'H1', 'CAC':'H2', 'CAA':'Q1','CAG':'Q2', 'AAT':'N1', 'AAC':'N2', 'AAA':'K1', 'AAG':'K2', 'GAT':'D1', 'GAC':'D2', 'GAA':'E1', 'GAG':'E2', 'TGT':'C1', 'TGC':'C2', 'TGG':'W', 'CGT':'R1', 'CGC':'R2', 'CGA':'R3', 'CGG':'R4', 'AGA':'R5', 'AGG':'R6', 'GGT':'G1', 'GGC':'G2', 'GGA':'G3', 'GGG':'G4'}

### this dictionary accounts for amino acid frequency. Most frequent AA is on the white keys. http://www.tiem.utk.edu/~gross/bioed/webmodules/aminoacid.htm
codon_to_key_dict = {'R1':'1','R2':'1', 'R3':'1', 'R4':'2', 'R5':'2', 'R6':'2', 'F1':'3', 'F2':'4', 'N1':'5', 'N2':'6', 'P1':'7', 'P2':'7', 'P3':'8', 'P4':'8','D1':'9', 'D2':'10', 'C1':'11', 'C2':'12', 'S1':'13', 'S2':'13', 'S3':'13', 'S4':'14', 'S5':'14', 'S6':'14', 'Q1':'15', 'Q2':'16', 'T1':'17', 'T2':'17','T3':'18', 'T4':'18', 'E1':'19', 'E2':'20', 'W':'21', 'W':'22', 'G1':'23', 'G2':'23', 'G3':'24', 'G4':'24', 'H1':'25', 'H2':'26', 'Y1':'27', 'Y2':'28', 'I1':'29', 'I2':'29','I3':'30', 'V1':'31', 'V2':'31','V3':'32', 'V4':'32', 'L1':'33', 'L2':'33', 'L3':'33', 'L4':'34', 'L5':'34', 'L6':'34', 'K1':'35', 'K2':'36', ' ':'37', ' ':'38', 'M':'39', 'M':'40', 'A1':'41', 'A2':'41', 'A3':'42', 'A4':'42'}

### keys are assigned a numeric value. the '2' version of each key is designated as the half note
key_dict = {'1':'C', '2':'C2', '3':'C#', '4':'C#2', '5':'D', '6':'D2', '7':'D#', '8':'D#2', '9':'E', '10':'E2', '11':'F', '12':'F2', '13':'F#', '14':'F#2', '15':'G', '16':'G2', '17':'G#', '18':'G#2', '19':'A', '20':'A2', '21':'A#', '22':'A#2', '23':'B', '24':'B2', '25':'C3', '26':'C4', '27':'C#3', '28':'C#4', '29':'D3', '30':'D4', '31':'D#3', '32':'D#4',  '33':'E3', '34':'E4', '35':'F3', '36':'F4', '37':'F#3', '38':'F#4', '39':'G3', '40':'G4', '41':' ', '42':' 2'}

DNA_sequence = input('Input DNA sequence:')

try:
    if re.findall(r'[^ATGC]', DNA_sequence):
        raise NotDNAError('non-ATGC characters found')
except NotDNAError:
    print('Non-ATGC characters found')
    exit

codons = re.findall(r'(.{3})', DNA_sequence)
#print(codons)

AA_list = []
for codon in codons:
    AA = nt_to_codon_dict[codon]
    AA_list.append(AA)

num_list = []    
for AA in AA_list:
    nums = codon_to_key_dict[AA]
    num_list.append(nums)

keynotes = []    
for num in num_list:
    key = key_dict[num]
    keynotes.append(key)

print(keynotes)


