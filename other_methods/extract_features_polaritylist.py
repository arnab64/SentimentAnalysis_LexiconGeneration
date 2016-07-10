'''
Extracts features from the raw data extracted from polarity list.
'''

ofile = open('processed_polist.txt','w')
orig_scores = []

def import_scores():
	ing1 = open('realresults.txt','r')
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
	'''
		1. total words
		2. number of words with non zero scores
		3. number of words with score +1
		4. number of words with score -1
		5. sum of scores
		6. +ve?-ve
	'''
	f1 = len(stuffx)
	f2 = 0
	f3 = 0
	f4 = 0 
	f5 = sum(stuffx)
	for j in range(f1):
		if stuffx[j]>0:
			f3+=1
			f2+=1
		elif stuffx[j]<0:
			f4+=1
			f2+=1
	if f3>f4:
		f6=1
	else:
		f6 = -1
	gog = [f1,f2,f3,f4,f5,f6]
	return gog	

def process():
	inf = open('detailed_polist.txt','r')
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