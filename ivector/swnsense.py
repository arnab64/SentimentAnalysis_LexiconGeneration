'''
Returns the total positive and negative scores of a word from sentiwordnet as the average of maximum 5 similar words!!
Steps:
	Finds the top five similar synsets to the word which is searched.
	Finds the positive and negative scores of each of the synsets.
	Returns the average positive and negative score.
'''

from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet as wn

def makesense(word):
	x1=wn.synsets(word)			#finding the similar wordnet synsets
	lenx=len(x1)
	pos1=0
	neg1=0
	sc=0
	res=[]
	
	if(lenx>5):
		lenx=5
	for i in range(lenx):		#loop to add the positive and negative scores for each synset
		x2=x1[i].name()		
		y1=swn.senti_synset(x2)
		try:
			pos2=y1.pos_score()
			neg2=y1.neg_score()
			sc=sc+1			
			pos1=pos1+pos2
			neg1=neg1+neg2

		except AttributeError:
			continue;
	if (sc!=0):
		positive=pos1/sc
		negative=neg1/sc
	else:	
		positive=0
		negative=0
	res.append(positive)
	res.append(negative)
	mytup=tuple(res)
	return mytup

