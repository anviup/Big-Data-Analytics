import scipy.io as sio
from math import ceil,floor
from statistics import mean
from numpy import square,sqrt,absolute
matfile = sio.loadmat( 'changed_param_2.mat' )
old_mat = sio.loadmat( 'learned_all_param_2_new.mat' )

v=[]
count=0
for i in range(0,150):
	v.append([])

for a in old_mat['new_ratings'][:,50:]:
	j=850
	for x in a:
		if int( x ) > 0:
			original_rating = matfile['p'][count,j]
			old_rating = old_mat['p'][count,j]
			v[j-850].append((x,original_rating,old_rating))
			
			#print x,' : ', original_rating,' : ',old_rating	
			#print 'rating',count,j,'=',original_rating, old_rating
			

		j=j+1

	count=count+1	
	#print count,a,original_rating,old_rating
f=0

for i in v:
	mea_round=[]
	mea_old_round=[]
	for j in i :
		mea_round.append( absolute( int( j[0]) - round( j[1] ) ) )
		mea_old_round.append( absolute( int( j[0] ) - round( j[2] ) ) )
		'''
    
	print len(mea_round),len(i)
	print mean(mea_round)
	print mean(mea_old_round)

	print sqrt( mean( square( mea_round ) ) )
	print sqrt( mean( square( mea_old_round ) ) )

	print mea_round.count( 0 )/float(len(mea_round))
	print mea_old_round.count( 0 )/float(len(mea_old_round))
	'''

	if mea_round.count( 0 )/float(len(mea_round)) >  mea_old_round.count( 0 )/float(len(mea_old_round)):
		f=f+1

print f

