#!/usr/bin/env python3

#the databases that we downloaded don't include the organism name in the header so we added it using this
#three things need to be added 1. database.fna file 2. new database file needs to opened and 3. the name of the organism in the new_database.write line (which adds it to the header)
import re

database = 'GCF_000026025.1_ASM2602v1_cds_from_genomic.fna'

open_database = open(database,'r')#original database
new_database = open('Chlamydia_abortus_cds.fna','w')#new database

for line in open_database:#opening the database
    line = line.rstrip()#strip the original database
    if line.startswith('>'):    #if it is a header line
        for found in re.finditer(r'(^>\S+)(.+)',line):#finding the reg expression
            new_database.write(found.group(1)+" Chlamydia abortus"+found.group(2)+'\n')#replacing the regular expression with the organism name in it
    else:
        new_database.write(line+'\n')#writing the sequence in addition to the header
        
        



