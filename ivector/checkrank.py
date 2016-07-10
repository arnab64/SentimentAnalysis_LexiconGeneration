#checks the rank of a word from the unified COCA list
import nltk, re, pprint
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def checkit(word1):
	with open("ivector/justrank.txt") as f:
	    content = f.readlines()
	
	for i in range(5000):
		hey=content[i]
		#print hey		
		a,b=hey.split()
		if(a==word1):
			rank=int(b)
			break;
	#print "i is:",i	
	if(i==4999):
		rank=5000
	return rank
