import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from ivector import ivector
import time
import os,glob

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')


scorefile_original = open('inputfiles/airscores.txt','r')		#this file is for original scores. No need to change this file.
origscores1 =  scorefile_original.read()
origscores2 = origscores1.split()

class lexicon:
	startfrom = 0

	def __init__(self):
		self.wordx = []
		self.scorex = []
		self.occurx = []
		self.loadlexicon()
		self.ofile = open("lexicons/lexicon.txt",'w')
		
	def listtextfiles(self,foldername):			#returns the name of all files inside the source folder. 		
		owd = os.getcwd()
		fld = foldername + "/"
		os.chdir(fld)					#this is the name of the folder from which the file names are returned.
		arr = []						#empty array, the names of files are appended to this array, and returned.
		for file in glob.glob("*.txt"):
			arr.append(file)
		os.chdir(owd)
		return arr
		
	def loadlexicon(self):
		presentfiles = self.listtextfiles('lexicons')
		if 'lexicon.txt' not in presentfiles:
			print "Initializing!..."
		else:
			tofrom1 = open('lexicons/status.txt','r')
			tofrom2 = tofrom1.read()
			tofrom3 = tofrom2.split()
			self.startfrom = int(tofrom3[1])
			tofrom1.close()
			infile = open("lexicons/lexicon.txt",'r')
			inlines = infile.readlines()
			lenv = len(inlines)
			for j in range(lenv):
				stuff = inlines[j].split()
				self.wordx.append(stuff[0])
				self.scorex.append(float(stuff[1]))
				self.occurx.append(int(stuff[2]))
			infile.close()
	
	def getstart(self):
		return self.startfrom
	
	def checkpresent(self,word):
		lenw = len(self.wordx)
		yeah = 1
		neah = -1
		for j in range(lenw):
			if self.wordx[j]==word:
				return yeah,self.scorex[j],j
		return neah,neah,-1
		
	def addword(self,word,score):
		lenw = len(self.wordx)
		#wordx[lenw] = word
		#scorex[lenw] = score
		self.wordx.append(word)
		self.scorex.append(score)
		self.occurx.append(1)
		
	def modifyword(self,word,score,indx):	
		#print "modify location",indx
		prevscr = self.scorex[indx]
		prevocc = self.occurx[indx]
		newocc = prevocc+1
		newscr = (prevscr*prevocc + score)/float(newocc)
		self.scorex[indx] = newscr
		self.occurx[indx] = newocc
		
	def processword(self,word,score):
		p,q,r = self.checkpresent(word)
		if p==-1:				#word is not present
			#print "word not present!"
			self.addword(word,score)
		else:
			#print "word already present at location",r
			self.modifyword(word,score,r)

	def writelexicon(self):
		for j in range(len(self.wordx)):
			#print self.wordx[j],self.scorex[j]
			self.ofile.write(self.wordx[j]+"	"+str(self.scorex[j])+"	"+str(self.occurx[j])+"\n")
			
	def getlexicon(self):
		return self.wordx,self.scorex,self.occurx

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
	
	#loading the input file.
	f = open('inputfiles/airline.txt')
	linex = f.readlines()
	len1= len(linex)
	lex = lexicon()
	startx = lex.getstart();
	dofor = 1000
	endx = 	startx + dofor		#provide the end position here
	print "creating lexicon from",startx,'till',endx
	numx = endx-startx;					
	for p in range(startx,endx):	
		thisline = linex[p]						
		vec = ivector.getweights(thisline)		#get the importance vector.

		thisline = thisline.lower()
		wordss = word_tokenize(thisline)
		thisscore = float(origscores2[p])
		for g in range(len(wordss)):
			if vec[g]!=0.0:
				#print wordss[g],vec[g]			show this to see all scores computed in real time
				scr = vec[g]*thisscore
				lex.processword(wordss[g],scr)
		perc = (p-startx)/float(numx)
		drawProgressBar(perc)
	drawProgressBar(1)
	lex.writelexicon()
	statfile = open('lexicons/status.txt','w')
	statfile.write(str(startx)+'	'+str(p+1))
	statfile.close()
	print("\n\n--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
	main()