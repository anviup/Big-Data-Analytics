#!/usr/bin/python

from math import sqrt
import ast
import sys

last_key = None
sum_xx, sum_xy, sum_yy, sum_x, sum_y, n = (0.0, 0.0, 0.0, 0.0, 0.0, 0)

def normalized_correlation(n, sum_xy, sum_x, sum_y, sum_xx, sum_yy):
                numerator = (n * sum_xy - sum_x * sum_y)
                try:denominator = sqrt(n * sum_xx - sum_x * sum_x) * sqrt(n * sum_yy - sum_y * sum_y)
		except: denominator=0                
		return numerator / denominator if denominator else 0

for line in sys.stdin:
    a,b = line.split(' | ')
    dict_val = ast.literal_eval(b.strip())
    item_p = int(a)
    item_pair, co_ratings = dict_val.keys()[0], dict_val.values()[0]
    #print type(item_pair), type(co_ratings)
    item_x, item_y = co_ratings[0],co_ratings[1]
    if last_key == None or last_key == item_p:
    	last_key = item_p
    
    else:
	#out_dct = dict()
        if n < 5: 
	    last_key = item_p
    	    sum_xx, sum_xy, sum_yy, sum_x, sum_y, n = (0.0, 0.0, 0.0, 0.0, 0.0, 0)
	    continue
	similarity = normalized_correlation(n, sum_xy, sum_x, sum_y, sum_xx, sum_yy)
    	#out_dct[(item_xname, item_yname)] = (similarity, n)
	#print out_dct
	print {(item_xname, item_yname): (similarity, n)}
	last_key = item_p
    	sum_xx, sum_xy, sum_yy, sum_x, sum_y, n = (0.0, 0.0, 0.0, 0.0, 0.0, 0)
    
    item_xname, item_yname = item_pair
    sum_xx += item_x * item_x
    sum_yy += item_y * item_y
    sum_xy += item_x * item_y
    sum_y += item_y
    sum_x += item_x
    n += 1
        
#print last_key,item_p
if last_key == item_p:
    #out_dct = dict()
    similarity = normalized_correlation(n, sum_xy, sum_x, sum_y, sum_xx, sum_yy)
    #out_dct[(item_xname, item_yname)] = (similarity, n)
    #print out_dct
    
    print {(item_xname, item_yname): (similarity, n)}
