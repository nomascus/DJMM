#!/usr/bin/env python3

#create a script that will count nucleotide compostion and amino acid composition 


#filename: count_nuc_amino_acid_composition.py
#owner: Bushra Gorsi


#======================
# Libraries
#======================

import Bio.Seq



#=====================
#variables 
#=====================

DNA_fasta_sequences = open ("sequences.fa" , "r")
nucleotide_comp = {}
nucleotide_comp2 ={}
amino_acid_comp ={}
seq_id = ''
final_dict ={}

#========================================================================
#                           script
#=========================================================================


for line in DNA_fasta_sequences:
    line = line.rstrip()
    if line.startswith('>'):
        remove_charac = line[1:]
        header_split= remove_charac.split(' ')
        seq_id = header_split[0]
        nucleotide_comp[seq_id] = ''
#print(nucleotide_comp)

    else:
        sequence = line
        if seq_id in nucleotide_comp:
            nucleotide_comp[seq_id] += sequence
        else:
            nucleotide_comp[seq_id] = sequence


#print(nucleotide_comp)

for seq_id in nucleotide_comp:
    sequence = nucleotide_comp[seq_id]
    a_count = sequence.count('A') 
    c_count = sequence.count('C')  
    g_count = sequence.count('G') 
    t_count = sequence.count('T') 
#print(a_count, c_count, g_count, t_count)
    nucleotide_comp2[seq_id] = {'nucA':a_count,'nucC':c_count,'nucG':g_count,'nucT':t_count}

#print(nucleotide_comp,nucleotide_comp2)

#Calculate amino acid composition

from Bio.Seq import Seq
from Bio.SeqUtils.ProtParam import ProteinAnalysis

for seq_id in nucleotide_comp:
    sequence = nucleotide_comp[seq_id]
    seqobj = Seq( sequence)
    seq_str=str(seqobj)
    protein = seqobj.translate()
    prot_str = str(protein)
    amino_acid_comp[seq_id] = prot_str

#print(amino_acid_comp)
   
for seq_id in amino_acid_comp:
    prot_str = amino_acid_comp[seq_id]
    prot_obj = ProteinAnalysis(prot_str)
    count_aa = prot_obj.count_amino_acids()
#print(count_aa) 
    amino_acid_comp[seq_id] = count_aa   
  
  
#print(amino_acid_comp)

#combining two dictionaries - created a 3D object with three keys

for seq_id in amino_acid_comp:
    final_dict[seq_id] = {'amino_acid' : amino_acid_comp[seq_id], 'nt' : nucleotide_comp2[seq_id]}

#print(final_dict)


import pandas as pd
import numpy as np

aa_df = pd.DataFrame.from_dict(amino_acid_comp)
#print(aa_df)
nt_df = pd.DataFrame.from_dict(nucleotide_comp2)
#print(nt_df)
seq_df = pd.concat([aa_df, nt_df])
print(seq_df)



    






  
 






      
 


    

    






















