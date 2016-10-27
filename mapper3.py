#!/usr/bin/python

import sys
import ast
from collections import defaultdict

song_sim = defaultdict(list)

for line in sys.stdin:
    #print len(line.strip())
    
    if len(line.strip()) == 0: continue
    inp_dct = ast.literal_eval(line)
    key = inp_dct.keys()[0]
    value = inp_dct.values()[0]
    
    song_sim[key[0]].append((key[1],value)) 
    song_sim[key[1]].append((key[0],value))
    
for temp in song_sim.keys():
    print {temp:song_sim[temp]}
