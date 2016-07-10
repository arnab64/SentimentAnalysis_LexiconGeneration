'''
This code uses the positive word list and negative word list to perform sentiment analysis.
If a sentence has more positive words than negative, it is positive, and vice versa.
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
		return 0

def find_sentiment(para):
	tokenized = word_tokenize(para)
	len2 = len(tokenized)
	sumx = 0
	foundscores = []
	for f in range(len2):
		foundscores.append(checkposneg(tokenized[f]))
	return foundscores

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

ofile = open('outputfiles/sentiment_raw_polaritylist.txt','w')

def writedown(arr):
	for j in range(len(arr)):
		ofile.write(str(arr[j])+'	')
	ofile.write('\n')

positive = readwords('opinion_lexicon/positive-words.txt')
negative = readwords('opinion_lexicon/negative-words.txt')

def main():
	start_time = time.time()
	print '\n'
	for p in range(1000,1800):		#from sentence 1000 to 1800.
		thisline = linex[p]
		thisline = thisline.lower()
		stopremoved = removestop(thisline)
		senti = find_sentiment(stopremoved)
		writedown(senti)
		drawProgressBar(float(p-1000)/800)
	ofile.close()	
	drawProgressBar(1.0)
	print("\n\n--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
	main()