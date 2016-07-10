'''
This code uses the positive word list and negative word list to perform sentiment 
analysis. It is a form of a rule based system.

Negativity is prioritized over positivity. i.e. If a sentence has a negative word, 
the sentence is negative. (which is true in most cases).
'''

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import compare_results
import time

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

f = open('inputfiles/airline.txt')
linex = f.readlines()
len1= len(linex)
stop_words = set(stopwords.words('english'))

def removestop(line):
    filtered_sentence = []
    word_tokens = word_tokenize(line)
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    glue= ' '
    return glue.join(filtered_sentence)

def readwords(lab):
    g = open(lab)
    wordss =[lines.rstrip() for lines in g.readlines()]
    return wordss

def checkposneg(wordc):
	if wordc in positive:
		return 1
	elif wordc in negative:
		return -1
	else:
		return 1

def countposneg(elems):
	#print elems
	pos = 0
	neg = 0
	for j in range(len(elems)):
		if elems[j]==-1:
			neg+=1
		if elems[j]==1:
			pos+=1
	if pos+neg==len(elems):
		return pos,neg
	else:
		print "mismatch!", pos+neg, len(elems)
		return 0,0

def find_sentiment(para):
	tokenized = word_tokenize(para)
	len2 = len(tokenized)
	sumx = 0
	foundscores = []
	for f in range(len2):
		foundscores.append(checkposneg(tokenized[f]))
	'''if -1 in foundscores:
		return -1
	elif 1 not in foundscores:
		return 1
	else:
		return 1'''
	ax,bx = countposneg(foundscores)
	if bx>0:					#if a negative word is present, sentence is negative
		if bx>2:
			return -3
		else:
			return -bx
	else:
		if ax>0:
			if ax>5:
				return 3
			else:
				return ax/2


def drawProgressBar(percent, barLen = 50):
	sys.stdout.write("\r")
	progress = ""
	for i in range(barLen):
		if i<int(barLen * percent):
			progress += "="
		else:
			progress += " "
	sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100))
	sys.stdout.flush()

positive = readwords('opinion_lexicon/positive-words.txt')
negative = readwords('opinion_lexicon/negative-words.txt')
	

def main():
	start_time = time.time()
	ofile = open('outputfiles/sentiment_posneglist.txt','w')
	print '\n'
	for p in range(1400,1800):
		thisline = linex[p]
		thisline = thisline.lower()
		stopremoved = removestop(thisline)
		senti = find_sentiment(stopremoved)
		ofile.write(str(senti)+'\n')
		drawProgressBar(float(p-1400)/400)
	ofile.close()	
	drawProgressBar(1.0)
	print("\n\n--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
	main()