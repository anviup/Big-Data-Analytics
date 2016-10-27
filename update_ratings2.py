import scipy.io as sio
import sys
import ast
import numpy
matfile = sio.loadmat('learned_all_param_2_new.mat')
copy_mat = matfile['p'].copy()
#print numpy.shape(matfile['p'])[1]   #,len(matfile['p'])

for line in sys.stdin:
    try:dct = ast.literal_eval(line)
    except: 
	print line
	break
    key = int(dct.keys()[0]) - 1
    value = dct.values()[0]
    
    #print [v for v in value]
    #sim_songs = [v[0] for v in value]
    sum_sim = sum((v[1][0] for v in value))
    #print matfile['p'][0][100],key,sum_sim
    for i in range(850,1000) :
	sum_val = 0
	#print i,key,matfile['p'][key,i],	
	for v in value: 
	    #print 'v[0]'+str(v[0]),'v[1]'+str(v[1]),
	    sum_val = sum_val + (matfile['p'][int(v[0])-1,i] * v[1][0])
            #print v,sum_val

	copy_mat[key,i] = (sum_val / sum_sim)        
	#print matfile['p'][key,i]
    	#break
    #break
    print key, 'done'

sio.savemat('changed_param_2_10.mat',{'p':copy_mat})
