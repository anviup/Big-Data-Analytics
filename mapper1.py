#!/usr/bin/python

import sys
#import timeit

#start = timeit.default_timer()
for line in sys.stdin:
    #output_dict = {}
    user_id, item_id, rating = line.split('|')
    #output_dict[user_id] = item_id, float(rating)
    #print output_dict
    print {user_id: (item_id, float(rating))}


#elapsed = timeit.default_timer() - start


#print elapsed
