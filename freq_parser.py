#!/usr/bin/env python3

#time: frequency parser

import sys

aubio_freq_output = sys.argv[1]

freq_dict = {}

with open('classicalfreq.txt','r') as file_obj:
        for line in file_obj:
            line = line.rstrip()
            line_split = line.split()
            time = line_split[0]
            frequency = line_split[1]
            freq_dict[time] = frequency

        print(freq_dict)
