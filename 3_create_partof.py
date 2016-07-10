'''
split the original results file to smaller ones. For example:
The corpus contained 1800 sentences, with 1800 scores.

We used 1000 sentences for creating the lexicon.
Of the remaining 800 sentences, we will use 400 for training, and 400 for testing.

This code creates those files containing the 400 and 800 scores.
'''

def main():
	inf = open('inputfiles/airscores.txt','r')
	inl = inf.read()
	stuff = inl.split()

	ofile = open('results/xresults.txt','w')
	for k in range(1400,1800):
		ofile.write(stuff[k]+'\n')

	ofile2 = open('outputfiles/realresults.txt','w')
	for k in range(1000,1800):
		ofile2.write(stuff[k]+'\n')

if __name__ == '__main__':
	main()