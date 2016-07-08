'''
This code is to compare the accuracy of the sentiment analysis.
The overall accuracy, accuracy of positive sentences and accuracy of negative sentences are computed!
'''

def integerize(arr):
	newarr = []
	for j in range(len(arr)):
		newarr.append(int(arr[j]))
	return newarr

def bipolarize(arr):
	newarr = []
	for j in range(len(arr)):
		if arr[j]>=0:
			newarr.append(1)
		else:
			newarr.append(-1)
	return newarr

def compare_files(fname1,fname2):					#usage: fname1 need to be the file with correct results.
	print "\ncomparing",fname1,"with",fname2
	scorefile_original = open(fname1,'r')			#fname2 can be the file with computed values.
	scores1 =  scorefile_original.read()
	scores2 = scores1.split()
	scores3 = integerize(scores2)
	sc1 = bipolarize(scores3)
	#print len(sc1),sc1
	
	scorefile_computed = open(fname2,'r')		
	comp1 = scorefile_computed.read()
	comp2 = comp1.split()
	sc2 = integerize(comp2)
	#print len(sc2),sc2
	
	if len(sc1)!=len(sc2):
		print "mismatch in file instances! Check your files properly!"
		return -1	
	realpos = 0 
	realneg = 0
	correctpos = 0
	correctneg = 0 
	foundneut = 0
	
	for k in range(len(sc1)):
		if sc1[k]==1:
			realpos+=1
			if sc2[k]==1:
				correctpos+=1
		else:
			realneg+=1
			if sc2[k]==-1:
				correctneg+=1
	#print 'total:',correct,'correct out of',len(sc2)
	#print 'positive:',correctpos,'correct out of',realpos
	#print 'negative:',correctneg,'correct out of',realneg
	#print correct,correctpos,correctneg,len(sc1)
	return float(correctpos+correctneg)/len(sc1),float(correctpos)/realpos,float(correctneg)/realneg
	
def main():
	acc = compare_files('inputfiles/airscores.txt','outputfiles/output_swn.txt')
	if acc!=-1:
		print '\ntotal accuracy:', round(acc[0]*100,2),'%'
		print 'positive accuracy:', round(acc[1]*100,2),'%'
		print 'negative accuracy:', round(acc[2]*100,2),'%'
	else:
		print "file_error!"

if __name__ == '__main__':
	main()