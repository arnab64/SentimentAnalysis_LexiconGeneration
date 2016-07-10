import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from ivector import ivector
import time

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')



stop_words = set(stopwords.words('english'))

scorefile_original = open('inputfiles/airscores.txt','r')		#this file is for original scores. No need to change this file.
origscores1 =  scorefile_original.read()
origscores2 = origscores1.split()

class lexicon:
	def __init__(self):
		self.wordx = []
		self.scorex = []
		self.occurx = []
		self.loadlexicon()
		self.lenw = len(self.wordx)

	def loadlexicon(self):
		infile = open("lexicons/lexicon.txt",'r')
		inlines = infile.readlines()
		lenv = len(inlines)
		for j in range(lenv):
			stuff = inlines[j].split()
			self.wordx.append(stuff[0])
			self.scorex.append(float(stuff[1]))
			self.occurx.append(int(stuff[2]))
		infile.close()
	
	def checkpresent(self,word):
		yeah = 1
		neah = -1
		for j in range(self.lenw):
			if self.wordx[j]==word:
				return yeah,self.scorex[j]
		return neah,neah
		

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
	
	f = open('inputfiles/airline.txt')
	linex = f.readlines()
	len1= len(linex)
	
	lex = lexicon()
	startx = 1000;
	endx = 1800;
	ofileq = open('outputfiles/detailed_scores_pure.txt','w')
	numx = endx-startx;					#change this number to get the number of lines to train.
	for p in range(startx,endx):	
		thisline = linex[p].lower()
		vec = ivector.getweights(thisline)
		wordss = word_tokenize(thisline)
		totalscore = 0
		for g in range(len(wordss)):
			if vec[g]!=0.0:
				stat, scr = lex.checkpresent(wordss[g])
				if stat==1:
					#totalscore+=scr
					ofileq.write(str(scr)+' ')
		ofileq.write('\n')
		perc = (p-startx)/float(numx)
		drawProgressBar(perc)
	drawProgressBar(1)
	print("\n\n--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
	main()