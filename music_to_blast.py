#!/usr/bin/env python3

#import modules to do the script
import time
import os
import re
from Bio import SearchIO
import webbrowser
from fpdf import FPDF
from IPython.display import Image

#running blast from the command line with the specifications to run blastn on the .fasta file as the query (one entry), the task is blastn-short which optimizes blast for short sequences, the max hsps is set to one, it is using the contstructed database (final_all_cds.fna - the one we constructed of 6 cds annotated databases), and the output is the test6.txt
cmd = "blastn -query test_seq.fasta -task 'blastn-short' -max_hsps 1 -db final_all_cds.fna -out test6.txt"
os.system(cmd)#running the command

filename = 'test6.txt' #bringing in the constructed blast text file

for QueryResult in SearchIO.parse(filename, 'blast-text'):#parses the query name
    print('Query name:',QueryResult.id)#prints the query name
    print('Query length:',QueryResult.seq_len)#prints the query length
query_name = 'Query name: '+str(QueryResult.id)#makes a variable to make things easier for the pdf
query_length = 'Query length: '+str(QueryResult.seq_len)#variable for pdf

for Hit in SearchIO.read(filename, 'blast-text'):#prints out the top hit id and description
    top_hit = Hit.description
    #print(top_hit)
    for found in re.finditer(r'(^\S?.+)\s(\[gene=)(\w+.?\w)',top_hit):
        organism = found.group(1)#finds the organism name of the top hit
        gene = found.group(3)#finds the gene name for the top hit
    break#break to only find the first hit and not go through the other ones
else:
    print("no hits")#if there are no hits, prints that
    organism = "no match organism"#sets the organism variable as none for the pdf
    gene = "no match gene"#sets the organism gene as none for the pdf

print('Organism:',organism)#prints the final determined organism
hit_organism = 'Organism: '+str(organism)#setting the variable for hit organism output
print('Gene:',gene)#prints the final determined gene
hit_gene = 'Gene: '+str(gene)#setting the variable for hit gene output

for alignment in SearchIO.read(filename, 'blast-text'):#parsing for scores/metrics
        for hsp in alignment.hsps:#prints out the hsp evalue score
                evalue = 'E-value: '+str(hsp.evalue)#evalue
                print('E-value:',hsp.evalue)
                hit_start = 'Hit start: '+str(hsp.hit_start)#start of the hit
                print('Hit start:', hsp.hit_start)
                hit_end = 'Hit end:'+str(hsp.hit_end)#end of the hit
                print('Hit end: ', hsp.hit_end)
                hit_identity = 'Nucleotide match: '+str(hsp.ident_num)#identity number
                print('Nucleotide match: ',hsp.ident_num)
        break#breaks to only pull the first
else:#if no hit, no evalue
    print("no evalue")
    evalue = "no evalue"

#the organismal visual output for the pdf and the variable name for the visualization
chlamydia = "    ,---. \n   / . . \ \n   |  _  | \n    \     /  \n    '___'  "

grapes = "    \-\       \n   __\ \ ,--.  \n  (``)\ \(  )-,  \n ( `` )(```)   ) \n  `--',.`-'(```) \n  (   X    )`-`,  \n   `-` `--`(   )  \n       (   )`-`,  \n        `-`(   ) \n            `-`   "

cat = "                         _\n                        / )\n                       ( (\n       A.-.A   .-''-.   ) )\n     / , , \_/        \\/ /\n     \ =t= ;       /    /\n      `--,\'  .__.|     /\n          || |    \\\\  | \n         ((,_|    ((,_\\"

c_elegans = "    ____\n   /    \ \n  '_,-,  \ \n      /   |\n     /   /\n    |   |     __    /\\\n    (    \___/  \___| |\n     \         _      /\n      \_______/ \____/"

mouse = "  (\__/)   \n /O O `.  \n   {O__,   \    {\n       / .  . )    \ \n       |-| '-' \    } \n      .(   _(   )_.'  \n  '---.~_ _ _&  "

fish = "       o                 o\n                  o    \n         o   ______      o \n           _/  (   \_  \n _       _/  (       \_  O  \n| \_   _/  (   (    0  \  \n|== \_/  (   (          | \n|=== _ (   (   (        |\n|==_/ \_ (   (          |\n|_/     \_ (   (    \__/\n          \_ (      _/\n            |  |___/\n           /__/"

sadness = "No match organism, no picture for you"#if no match, no picture

if organism == "Chlamydia abortus":#if/elif/else loop to specify the picture based on 
    picture = chlamydia            #what the resulting organism is
    red =255                       #we are specifying what colour the organism should be 
    green =102                     #printed in (different for each organism)
    blue =175                       
    alignment = "C"                #also specifying whether it should be aligned left or center
elif organism == "Felis_catus":
    picture = cat
    red = 255
    green =153
    blue =51
    alignment = "C"
elif organism == "Caenorhabditis elegans":
    picture = c_elegans
    red = 204
    green =204
    blue =0
    alignment = "L"
elif organism == "Vitis vinifera":
    picture = grapes
    red = 127
    green = 0
    blue = 255
    alignment = "L"
elif organism == "Danio rerio":
    picture = fish
    red =51
    green =153
    blue =255
    alignment = "L"
elif organism == "Mus musculus":
    picture = mouse
    red =160
    green = 160
    blue = 160
    alignment = "C"
else:
    picture = sadness
    red =255
    green =0
    blue =0
    alignment = "L"

pdf = FPDF()#creating a PDF file
pdf.add_page()#adding a page to the newly created PDF file
pdf.set_font('Courier',size=24)#specifying the font and size
pdf.cell(100,20, txt = query_name, ln=1, align="L")#first line is query name aligned left
pdf.cell(100,20, txt = query_length, ln=1, align="L")#second line is query length
pdf.cell(100,20, txt = hit_organism, ln=1, align="L")#third line is hit organism
pdf.cell(100,20, txt = hit_gene, ln=1, align="L")#fourth line is hit gene
pdf.cell(100,20, txt = evalue, ln=1, align="L")#fifth line is the evalue
pdf.set_text_color(int(red),int(green),int(blue))#changing the colour of the subsequent text
pdf.multi_cell(200,10, txt = picture, align=alignment)#over multiple lines, we are printing out the final organism picture

ts = str(int(time.time()))#makes a time stamp so we don't write over files
blast_dir = '/var/www/html/blast_pdfs'#the directory for where the pdf gets created
blast_filename = blast_dir + "/Blast_visualization" + ts + ".pdf"#the file name/where to find it
pdf.output(blast_filename)#making the file? I think

print("Your run is complete; please see PDF!")#some of the other metrics will be printed but this tells us that it is completely done running



