from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import checkrank
import swnsense
import nltk

stop_words = set(stopwords.words('english'))

def getweights(sentence):
	sent=word_tokenize(sentence)
	lenx=len(sent)

	group1=['NNS','NN']												## 1
	group2=['NNP','NNPS','CD','IN','TO','CC','.',',']				## 0
	group3=['VB','VBG','VBZ','VBN','VBP','VBD']						## 4
	group4=['JJ','JJR','JJS']										## 4
	group5=['RB','RBR','RBS']										## 2

	def posweights(poslist):						## ranks the importance of the words as per their POS tags
		lenx = len(poslist)
		posw=[]
		for j in range(lenx):		
			y=poslist[j]		
			if y in group1:
				posw.append(1)					
			elif y in group2:
				posw.append(0)				
			elif y in group3:
				posw.append(4)				
			elif y in group4:
				posw.append(4)				
			elif y in group5:
				posw.append(2)					
			else:
				posw.append(0)
		return posw

	def rankweight(sente,partsos):			
		lenxx=len(sente)
		ranks=[]	
		for k in range(lenxx):		
			if sente[k]=='is':
				rank=10
			else:
				rank=checkrank.checkit(sente[k])
			if partsos[k] not in group2:				
				ranks.append(rank)
			else:				
				ranks.append(0)	
		return ranks	

	def checkallzero(vec1):
		len1=len(vec1)
		s1=sum(vec1)
		if s1==0:
			return 0
			
	def swnweight(sentence1):
		lenx=len(sent3)
		swnr=[]
		for j in range(lenx):
			if sent3[j] not in stop_words:
				we=swnsense.makesense(sent3[j])	
				posn=we[0]
				negn=we[1]
				scrn=posn+negn
				swnr.append(scrn)
			else:
				swnr.append(0)
		return swnr		
	
	def extractpos(newpos):					#extracts the 'parts of speech' of each word sequentially
		lenp=len(newpos)
		justpos=[]	
		for g in range(lenp):
			a,b=newpos[g]
			if a!='is':
				justpos.append(b)
			else:
				justpos.append('CC')
		return justpos	

	def normalizevec(listy):			#normalizes all vectors such that sum is 1
		lent=len(listy)
		sum1=0
		listz=[]
		for k in range(lent):
			sum1=sum1+listy[k]
		for k in range(lent):
			try:
				val=listy[k]/float(sum1)
				listz.append(val)
			except ZeroDivisionError:
				listz.append(0)	
		return listz

	def avgnorm_two(vec1,vec2):			#finds average of two normalized vectors
		lenx=len(vec1)
		kk=[]		
		for j in range(lenx):
			cc=(vec1[j]+vec2[j])/float(2)
			kk.append(cc)
		return kk
	
	newpos1=nltk.pos_tag(sent)
	poslist=extractpos(newpos1)
	vec1=posweights(poslist)				
	vec2=rankweight(sent,poslist)
	norm1=normalizevec(vec1)
	norm2=normalizevec(vec2)
	normavg=avgnorm_two(norm1,norm2)	
	return normavg