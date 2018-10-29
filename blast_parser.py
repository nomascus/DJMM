#!/usr/bin/env python3

from Bio import SearchIO#parser for Blast text output files

filename = 'test5.txt'
#filename = blastoutput.txt #we will have the general output from the blast be blastoutput.txt that way it is easy to bring in

for QueryResult in SearchIO.parse(filename, 'blast-text'):#parses the query name
	print('Query name:',QueryResult.id)#prints the query name

for Hit in SearchIO.read(filename, 'blast-text'):#prints out the top hit id and description
	print('Top hit:',Hit.id,Hit.description) 
	break

#for result in SearchIO.read(filename,'blast-text'):
#	for hit in result.hits:
#		print('E-value:',hit.hit_evalue)
	
for alignment in SearchIO.read(filename, 'blast-text'):	
	for hsp in alignment.hsps:#prints out the hsp evalue score
		print('E-value:',hsp.evalue)
		print('Hit start:', hsp.hit_start)
		print('Hit end:', hsp.hit_end)
	break






