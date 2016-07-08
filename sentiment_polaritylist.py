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
	if -1 in foundscores:
		return -1
	elif 1 not in foundscores:
		return 1
	else:
		return 1

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
	for p in range(len1):
		thisline = linex[p]
		thisline = thisline.lower()
		stopremoved = removestop(thisline)
		senti = find_sentiment(stopremoved)
		ofile.write(str(senti)+'\n')
		drawProgressBar(float(p)/len1)
	ofile.close()	
	drawProgressBar(1.0)
	print '\n'
	acc = compare_results.compare_files('inputfiles/airscores.txt','outputfiles/sentiment_posneglist.txt')
	if acc!=-1:
		print '\ntotal accuracy:', round(acc[0]*100,2),'%'
		print 'positive accuracy:', round(acc[1]*100,2),'%'
		print 'negative accuracy:', round(acc[2]*100,2),'%'
	else:
		print "file_error!"
	print("\n\n--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
	main()