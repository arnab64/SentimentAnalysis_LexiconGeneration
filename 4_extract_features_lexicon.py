'''
Pre-classification phase:

Extracts features from the raw data found after getting the scores from lexicon for each sentence.
i.e. this code creates the dataset which we use for classification.

The features extracted are:

		1. number of important words
		2. min
		3. max
		4. number of negative
		5. number of positive
		6. number of negative above threshold (-0.25)
		7. number of positive above threshold (0.25)
		8. sum of negative
		9. sum of positive
		10. sum of negative above threshold
		11. sum of positive above threshold
		12. f8>f9?
		13. f10>f11?
'''

ofile = open('outputfiles/processed.txt','w')
orig_scores = []

def import_scores():
	ing1 = open('outputfiles/realresults.txt','r')
	ing2 = ing1.read()
	ing3 = ing2.split()
	for j in range(len(ing3)):
		orig_scores.append(int(ing3[j]))
	print orig_scores[:10]

def writedown(yx,kk):
	for g in range(len(yx)):
		ofile.write(str(yx[g])+'	')
	ofile.write(str(orig_scores[kk])+'\n')

def getfeatures(stuffx):
	print "stuffx:", stuffx
	f1 = len(stuffx)
	try:
		f2 = min(stuffx)
		f3 = max(stuffx)
	except:
		f2 = 0
		f3 = 0
	f4 = 0
	f5 = 0
	f6 = 0
	f7 = 0
	f8 = 0
	f9 = 0
	f10 = 0
	f11 = 0
	for k in range(f1):
		if stuffx[k]>=0.0:
			f5+=1
			f9+=stuffx[k]
			if stuffx[k]>=0.25:
				f7+=1
				f11+=stuffx[k]
		else:
			f4+=1
			f8+=stuffx[k]
			if stuffx[k]<-0.25:
				f6+=1
				f10+=stuffx[k]
	if f8>f9:
		f12 = 1
	else:
		f12 = 0
	if f10>f11:
		f13 = 1
	else:
		f13 = 0
	gog = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13]	
	#print gog
	return gog	

def process():
	inf = open('outputfiles/detailed_scores_pure.txt','r')
	inl = inf.readlines()
	lenx = len(inl)
	for j in range(lenx):
		stuffed = []
		stuff = inl[j].split()
		for k in range(len(stuff)):
			stuffed.append(float(stuff[k]))
		feats = getfeatures(stuffed)
		writedown(feats,j)

def main():
	import_scores()
	process()

if __name__=='__main__':
	main()