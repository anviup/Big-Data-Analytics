#!/usr/bin/python

import sys
import ast

last_key = None
last_val = []
for line in sys.stdin:
    if len(line.strip()) == 0: 
	#print 'yolo'
	continue
    a,b = line.split(' | ')
    
    input_dct = ast.literal_eval(b.strip())
    val = input_dct.values()[0]
    key = input_dct.keys()[0]
    #print 'val',val
    if last_key != None and last_key!= key:
	last_val.sort(reverse=True, key=lambda x: x[1])
	print {last_key:last_val[0:10]}
	last_val = val 
	
    else:
        last_val += val

    last_key = key
    #print 'val',val
    #print 'lval',last_val
    

#print last_key,key
if last_key == key:
    last_val.sort(reverse=True, key=lambda x: x[1])
    print {last_key:last_val[0:10]}

    




