'''
In this code we use sentiwordnet to find the sentiment of the text. 
It takes up a lot of time to run though, because searching sentiwordnet takes up some time.
I will code a faster version of this code, which uses some kind of cache.
'''

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from ivector import swnsense
import compare_results
import sys  
import time


reload(sys)  
sys.setdefaultencoding('utf8')

f = open('inputfiles/airline.txt')
linex = f.readlines()
len1= len(linex)

stop_words = set(stopwords.words('english'))

scorefile_original = open('inputfiles/airscores.txt','r')		#this file is for original scores. No need to change this file.
origscores1 =  scorefile_original.read()
origscores2 = origscores1.split()

checked=0
correct=0
foundpos=0
foundneg=0
realpos=0
realneg=0 
correctpos=0 
correctneg=0

def performance(nox,val):			#finds the real time performance of the sentiment analysis.
	global checked, correct, foundpos, foundneg, realpos, realneg, correctpos, correctneg
	if origscores2[nox]=='1':
		realpos+=1
		if val=='1':
			foundpos+=1
			correctpos+=1
		else:
			foundneg+=1
	else:
		realneg+=1
		if val=='-1':
			foundneg+=1
			correctneg+=1
		else:
			foundpos+=1
	checked+=1
	perc = (correctpos+correctneg)/float(realpos+realneg)
	if realpos==0:
		realpos=1
	if realneg==0:
		realneg=1
	posperc = float(correctpos)/realpos
	negperc = float(correctneg)/realneg
	return checked, perc, posperc, negperc

def removestop(line):				#stopword removal
    filtered_sentence = []
    word_tokens = word_tokenize(line)
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return ' '.join(filtered_sentence)

def find_sentiment_sentence(senten):
	senten = senten.lower()
	newline = removestop(senten)
	text = newline.split()
	leng = len(text)
	totalpos = 0
	totalneg = 0
	for h in range(leng):
		scores = swnsense.makesense(text[h])
		totalpos+=scores[0]
		totalneg+=scores[1]
	if totalpos>totalneg:
		return '1'
	elif totalpos<totalneg:
		return '-1'
	else:
		return '1'
		
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

def main():	
	start_time = time.time()
	ofile = open('outputfiles/output_swn.txt','w')	
	print '\n'
	for p in range(len1):	
		thisline = linex[p]
		final = find_sentiment_sentence(thisline)
		ofile.write(final+'\n')
		perf = performance(p,final)
		#print "accuracy=",perf[1]*100,'% ; positive_acc',perf[2]*100,'% ; negative_acc',perf[3]*100,'%'
		drawProgressBar(float(p)/len1)
	ofile.close()
	drawProgressBar(1.0)
	print '\n'
	acc = compare_results.compare_files('inputfiles/airscores.txt','outputfiles/output_swn.txt')
	if acc!=-1:
		print '\ntotal accuracy:', round(acc[0]*100,2),'%'
		print 'positive accuracy:', round(acc[1]*100,2),'%'
		print 'negative accuracy:', round(acc[2]*100,2),'%'
	else:
		print "file_error!"
	print("\n\n--- %s seconds ---" % (time.time() - start_time))
	
if __name__ == '__main__':
	main()
	