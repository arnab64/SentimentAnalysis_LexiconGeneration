##Automated lexicon generation for sentiment analysis
 
Language used: *Python*

This repository contains three codes

1. Sentiment analysis using positive and negative word polarity list 
	*code: sentiment_polaritylist.py
2. Sentiment analysis using sentiwordnet
	*code: sentiment_swn.py
3. Corpus-based Automated generation of sentiment lexicon
	*code: to be uploaded soon

Besides these major codes, we I have also included the code for *importance-vector* inside the folder *ivector*. The importance vector of a sentence returns a vector of length equal to the number of words of the sentence, with the weight corresponding to  each word as element of the vector. The weights are computed based on their sentiwordnet scores and word popularity ranking.
	
Run these files like:	
```
python sentiment_polaritylist.py
python setiment_swn.py
```