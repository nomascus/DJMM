#!/usr/bin/env python3

#filename: fasta2sequence.py

#output: Generate a DNA sequence from one fasta file
import sys

fasta_sequence = sys.argv[1]

open_fasta_sequence = open (fasta_sequence , "r")
dna_seq = ''

for line in open_fasta_sequence:
    line = line.rstrip()
    if not line.startswith('>'):
        dna_seq +=line
