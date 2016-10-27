#!/usr/bin/python

import sys
import ast

last_key = None
item_count = 0
item_sum = 0
final = []
    
for line in sys.stdin:
    
    input_dict = ast.literal_eval(line)
    
    values = input_dict.values()
    user_id = input_dict.keys()[0]
    #print type(user_id),values[0][0]

    if user_id == last_key or last_key==None:
        last_key = user_id 
        item_id, rating = values[0][0],values[0][1]
        item_count += 1
    	item_sum += rating
	#print rating
    	final.append((item_id, rating))
    else:
	 
	#output_dict = dict()
        #output_dict[last_key] = (item_count, item_sum, final)
	#print output_dict
	print {last_key: (item_count, item_sum, final)}
	
	last_key = user_id
        item_id, rating = values[0][0],values[0][1]
        item_count = 1
	item_sum = rating
	final = []
    	final.append((item_id, rating))

#print last_key,user_id    
if last_key == user_id:
    #output_dict = dict()
    #output_dict[last_key] = (item_count, item_sum, final)
    #print output_dict   
    print {last_key: (item_count, item_sum, final)}
