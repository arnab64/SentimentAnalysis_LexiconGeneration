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

def compare(fname1,fname2):
	print "\ncomparing",fname1,"with",fname2
	scorefile_original = open(fname1,'r')			#fname2 can be the file with computed values.
	scores1 =  scorefile_original.read()
	scores2 = scores1.split()
	sc1 = integerize(scores2)
	
	scorefile_computed = open(fname2,'r')		
	comp1 = scorefile_computed.read()
	comp2 = comp1.split()
	sc2 = integerize(comp2)

	if len(sc1)!=len(sc2):
		print "mismatch in file instances! Check your files properly!"
		return -1

	posx = 0
	negx = 0
	poscorr = 0
	negcorr = 0 
	for j in range(len(sc1)):
		if sc1[j]>=0:
			posx+=1
			if sc1[j]==sc2[j]:
				poscorr+=1
		elif sc1[j]<0:
			negx+=1
			if sc1[j]==sc2[j]:
				negcorr+=1	
	return float(poscorr+negcorr)/len(sc1), float(poscorr)/posx, float(negcorr)/negx

def bipolar_compare(fname1,fname2):					#usage: fname1 need to be the file with correct results.
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
	comp3 = integerize(comp2)
	sc2 = bipolarize(comp3)
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
	
def justcompare(fname1,fname2):
	acc = bipolar_compare(fname1,fname2)
	if acc!=-1:
		print '\ntotal bipolar accuracy:', round(acc[0]*100,2),'%'
		print 'positive bipolar accuracy:', round(acc[1]*100,2),'%'
		print 'negative bipolar accuracy:', round(acc[2]*100,2),'%'

		acc2 = compare(fname1,fname2)
		print '\ntotal real accuracy:', round(acc2[0]*100,2),'%'
		print 'positive real accuracy:', round(acc2[1]*100,2),'%'
		print 'negative real accuracy:', round(acc2[2]*100,2),'%'
	else:
		print "file_error!"

def main():
	justcompare('results/xresults.txt','results/svmresults.txt')
	#justcompare('results/xresults.txt','results/sentiment_added.txt')
	

if __name__ == '__main__':
	main()