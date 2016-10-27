import scipy.io as sio
from math import ceil,floor
from statistics import mean
from numpy import square,sqrt,absolute
matfile = sio.loadmat( 'changed_param_2.mat' )
old_mat = sio.loadmat( 'learned_all_param_2.mat' )

#for i in range( 15 ):
#print matfile['p'][[11 ,67 ,225,336,357,444,635,679],0],old_mat['p'][[11 ,67 ,225,336,357,444,635,679],0]

count = 5000
mea_ceil = []
mea_floor = []
mea_old_ceil = []
mea_round = []
mea_old_round = []
#
mea_old_floor = []
for a in old_mat['new_ratings'][:,50:]:
	j=850
	for x in a:
		if int( x ) > 0:
			original_rating = matfile['p'][count,j]
			old_rating = old_mat['p'][count,j]
			#print 'rating',count,j,'=',original_rating, old_rating
			mea_ceil.append( absolute( int( x ) - ceil( original_rating ) ) )
			mea_round.append( absolute( int( x) - round( original_rating ) ) )
			mea_floor.append( absolute( int( x) - floor( original_rating ) ) )
			mea_old_ceil.append( absolute( int( x ) - ceil( old_rating ) ) )
			mea_old_floor.append( absolute( int( x ) - floor( old_rating ) ) )
			mea_old_round.append( absolute( int( x ) - round( old_rating ) ) )

		j=j+1

	count=count+1	
	#print count,a,original_rating,old_rating


print len(mea_ceil)
print mean( mea_ceil ),mean( mea_floor ), mean(mea_round)
print mean( mea_old_ceil ),mean( mea_old_floor ),mean(mea_old_round)

print sqrt( mean( square( mea_ceil ) ) ),sqrt( mean( square( mea_floor ) ) ),sqrt( mean( square( mea_round ) ) )
print sqrt( mean( square( mea_old_ceil ) ) ),sqrt( mean( square( mea_old_floor ) ) ),sqrt( mean( square( mea_old_round ) ) )

print mea_ceil.count( 0 )/float(len(mea_ceil)),mea_floor.count( 0 )/float(len(mea_floor)),mea_round.count( 0 )/float(len(mea_round))
print mea_old_ceil.count( 0 )/float(len(mea_old_ceil)),mea_old_floor.count( 0 )/float(len(mea_old_floor)),mea_old_round.count( 0 )/float(len(mea_old_round))

