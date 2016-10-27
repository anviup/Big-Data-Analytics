#!/usr/bin/python

from itertools import combinations
import sys
import ast

for line in sys.stdin:
    
    try:val = ast.literal_eval(line)
    except: 
	print line
	break
    dict_val = val.values()
    item_count, item_sum, rating = dict_val[0][0], dict_val[0][1], dict_val[0][2]
    sort_rating = sorted(rating, key=lambda x: x[1]) 
    
    mean = sum(v[1] for v in rating)/len(rating)
    median = (rating[0][1] + rating[-1][1])/2
    a,b = [(median,mean), (mean,median)][mean > median]
 
    first_bkt = [(x,y) for (x,y) in rating if y <= a]
    second_bkt = [(x,y) for (x,y) in rating if  a < y <= b]
    third_bkt = [(x,y) for (x,y) in rating if b < y]

    #print 'first_bkt', len(first_bkt), first_bkt
    #print 'second_bkt',len(second_bkt), second_bkt
    #print 'third_bkt',len(third_bkt),third_bkt
    
    for i in [first_bkt,second_bkt,third_bkt]:    
	for item1, item2 in combinations(i, 2):
            #print item1, item2
	    print item1[0]+item2[0], '|',{(item1[0], item2[0]): (item1[1], item2[1])}
    
