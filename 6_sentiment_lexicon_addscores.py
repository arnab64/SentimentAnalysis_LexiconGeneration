'''
Using the raw scores from lexicon and computing sentiment.
Sentiment is computed as:

sentiment(sentence) = sum of scores of all words in sentence 
					*  3/standard deviation (total scores of all sentences in test dataset)

'''

import math
import numpy as np

ofile = open('results/sentiment_added.txt','w')
orig_scores = []

def import_scores():
	ing1 = open('outputfiles/realresults.txt','r')
	ing2 = ing1.read()
	ing3 = ing2.split()
	for j in range(len(ing3)):
		orig_scores.append(int(ing3[j]))
	
def process_score(sc,stx):
	#print "sc=",sc
	if sc>=0.0:
		scr = math.ceil(sc*3/float(stx))
		if scr>3:
			scr=3
	else:
		scr = math.floor(sc*3/float(stx))
		if scr<-3:
			scr=-3
	return scr

def writedown(yx,kk):
	for g in range(len(yx)):
		ofile.write(str(yx[g])+'	')
	ofile.write(str(orig_scores[kk])+'\n')

def stdev(arr):
	meanx = np.mean(arr)
	shp0 = len(arr)
	totsum = 0
	for el in arr:
		ant = (el-meanx)*(el-meanx)	
		totsum+=ant
	return math.sqrt(totsum/shp0)

def process():
	inf = open('outputfiles/detailed_scores_pure.txt','r')
	inl = inf.readlines()
	lenx = len(inl)
	allscores = []
	for j in range(lenx):
		stuffed = []
		stuff = inl[j].split()
		for k in range(len(stuff)):
			stuffed.append(float(stuff[k]))
		feats = sum(stuffed)
		allscores.append(feats)
	stdx = stdev(allscores)
	for h in range(400,800):
		fin = process_score(allscores[h],stdx)
		fin = int(fin)
		ofile.write(str(fin)+'\n')

def main():
	process()

if __name__=='__main__':
	main()
