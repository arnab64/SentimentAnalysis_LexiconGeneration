## Real Part of Speech tagging

#import refinetags
import nltk,re,pprint
import sys
#import aposres
import checkrank

reload(sys)
sys.setdefaultencoding('latin1')

def postag(raw):										## part1: 	removes comma and places and
	raw = "".join(c for c in raw if c not in ('!','.',':','?',';','``','&','"',"'"))	
	raw=raw.split()
	#common=open('common1.txt').read()					##insert the file of common words if they are to be decapitalized
	#common=common.split()	
	exclude=open('exclude.txt').read()					##insert the file of words which are to be excluded
	exclude=exclude.split()	
	verbies=open('justverbs.txt').read()				##insert the file of verbs which are to be certainly decapitalized
	verbies=verbies.split()


	x=len(raw)

	raw2=[]
	for i in range(x):
		raw2.append(raw[i])

	def checkcomma(word1):
		lenw=len(word1)
		for k in range(lenw):
			if(word1[k]==','):
				return 1
		return 0

	def checkhyphen(word2):
		lenw=len(word2)	
		for j in range(lenw):
			if(word2[j]=='-'):
				return 1
		return 0	

	def returnhypos(word2):
		lenw=len(word2)
		for k in range(lenw):
			if(word2[k]=='-'):
				return k

	def updateshift():
		z=len(raw2)
		diff=z-x
		return diff

	for f in range(x):
		s=checkcomma(raw[f])
		hy=checkhyphen(raw[f])
		if(s==1):
			df=updateshift()
			old=raw[f]
			lenn=len(old)		
			new=old[:lenn-1]
			raw2.pop(f+df)
			raw2.insert(f+df,'and')
			raw2.insert(f+df,new)
			
		if(hy==1):
			old=raw[f]
									
			df=updateshift()
			position=returnhypos(old)
			first=old[:position]
			second=old[position+1:]
										
			raw2.pop(f+df)
			raw2.insert(f+df,second)
			raw2.insert(f+df,'and')
			raw2.insert(f+df,first)

	y=len(raw2)
	newsent=" ".join(raw2)
									
	#raw2=aposres.proc(raw2)				

	for t in range(y):					
		lowered=raw2[t].lower()
		if raw2[t] in exclude:
			continue;
		rank=checkrank.checkit(lowered)		
		if lowered in verbies:
			raw2[t]=raw2[t].lower()
			continue;			
		#if lowered in common:					##enable these two lines if some common words are to be decapitalized
		#	raw2[t]=raw2[t].lower()
		if (rank<4999):
			raw2[t]=raw2[t].lower()

	tagprev = nltk.pos_tag(raw2)				##pos tagging done here
	#tags=refinetags.reftag(tagprev)			##enable this if some domain specific refinement is to be done
	return tagprev