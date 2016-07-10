##Automated lexicon generation for sentiment analysis
 
Language used: *Python*

This repository contains the codes for generation of lexicon and using it to compute sentiment of sentences using machine learning approach (classification).

The methodology will be described in detail in the report. However, the steps can be briefly mentioned as follows:
1. Generation of the corpus-dependent lexicon from a part of an annotated corpus.
2. Using the generated lexicon to find the raw scores of words from the rest of the corpus.
3. Extracting relevant features from the raw scores.
4. Training and testing the SVM classifier on the extracted features.
5. Comparing the resulting sentiments with the original scores.

Besides these major codes, we I have also included the code for *importance-vector* inside the folder *ivector*. The importance vector of a sentence returns a vector of length equal to the number of words of the sentence, with the weight corresponding to  each word as element of the vector. The weights are computed based on their sentiwordnet scores and word popularity ranking.
	
To run the above two codes, just execute the corresponding Python codes
```
python sentiment_polaritylist.py
python sentiment_swn.py
```

In order to generate the lexicon, edit the *generate_lexicon.py* file to provide how many instances to train on.
```
python generate_lexicon.py
``` 
After the lexicon is generated, you can use the lexicon to evaluate the sentiment by using:
```
python uselexicon.py
```