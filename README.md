##Automated lexicon generation for sentiment analysis
 
Language used: *Python*

This repository contains the codes for generation of lexicon and using it to compute sentiment of sentences using machine learning approach (classification).

#####Methodology
The methodology will be described in detail in the report which will be shared in a link here. The steps can be briefly mentioned as follows:

- Generation of the corpus-dependent lexicon from a part of an annotated corpus.
- Using the generated lexicon to find the raw scores of words from the rest of the corpus.
- Extracting relevant features from the raw scores.
- Training and testing the SVM classifier on the extracted features.
- Comparing the resulting sentiments with the original scores.

#####Dataset
The dataset that I used here is a self-made dataset for sentiment analysis, the details of which are presented below
- Contains 1800 instances of news headlines relating to airlines (Cathay Pacific, Air India, British Airways etc.)
- Each sentence is manually annotated by two persons, and the instances which have been equally annotated by the two persons are kept.
- Sentiment is annotated on a scale from -3 to +3, with -3 being 'very bad news' and +3 being 'very good news'

#####Usage
Generate the lexicon using. As lexicon generation is a time consuming process, I have developed the code to work part by part. You can change the variable *dofor* to whatever value you want and it resumes the lexicon generation from the last instance for *dofor* more instances. Like, initially using *dofor=250*, generates lexicon from 0 to 250, the second time it generates from 250 till 500, and so on.	
```
python 1_generate_lexicon.py
```

After the generation of lexicon, we use the lexicon for further processing. For the rest of the instances which were not used in generation of the lexicon, for each sentence, we extract the raw scores of individual words from the lexicon. 
```
python 2_use_generated_lexicon.py
```

Now, to extract the features from the raw scores, we have the following code. The features extracted are (number of words with scores, highest score, least score, number of positive scores and negative scores, positive>negative? , etc)
```
python 4_extract_features_lexicon.py
``` 

After the features are generated, the data is ready for classification. We use *Support Vector Machine* classification available in *scikit-learn* for our purpose. Half of the data is used for training and the remaining half for testing. Modify the indexes in the code accordingly. The results of the classification are available in the *results* folder.
```
python 5_svm_classification.py
```

After classification, we need to measure the performance of classification. We measure the sentiment bipolar performance i.e. performance of declaring a sentiment as positive or negative, with no other information. Also, we measure qualitative performance i.e. performance of finding if a sentiment is positive or negative along with qualitative information i.e. just positive, more positive, very positive etc, likewise bad, very bad etc. In our experiments we have taken scores in the range -3 to +3, -3 being extremely bad and +3 means extremely good.
```
python 7_compare_results.py
```

Miscellaneous
---------------------------
Besides these major codes, we I have also included the code for a few utilities which can be used.

Importance vector
 *importance-vector* which can be found inside the folder *ivector*. The importance vector of a sentence returns a vector of length equal to the number of words of the sentence, with the weight corresponding to  each word as element of the vector. The weights are computed based on their sentiwordnet scores and word popularity ranking.

swnsense
swnse

All done. So, these are the results I obtained on using the *airline-sentiment* dataset, available inside the folder *inputfiles*

- Bipolar prediction accuracy = 86.75 %
- Bipolar positive prediction accuracy = 96.17 %
- Bipolar negative prediction accuracy = 62.83 %
- Qualitative prediction accuracy = 69.75 %
- Qualitative positive prediction accuracy = 85.02 %
- Qualitative negative prediction accuracy = 30.97 % 