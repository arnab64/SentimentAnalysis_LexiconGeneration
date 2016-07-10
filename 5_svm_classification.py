'''
We use this code for classifying the sentiment after extracting the features.

Classification is done using Support Vector Machines (SVMs)
I have also included KNearestNeighborsClassifier.
'''

import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

class predict:
	arr1 = np.loadtxt('outputfiles/processed.txt')
	print arr1.shape
	train_x = arr1[:400,:-1]
	train_y = arr1[:400,-1]
	test_x = arr1[400:,:-1]
	test_y = arr1[400:,-1]
	print train_x.shape
	#print train_y
	print test_x.shape
	#print test_y

	def writedown(self,stuff,ofname):
		ofile = open(ofname,'w')
		for j in range(len(stuff)):
			lol = int(stuff[j])
			ofile.write(str(lol)+'\n')

	def svm_predict(self):
		clf = SVC(kernel='rbf')
		clf.fit(self.train_x,self.train_y)
		hola = clf.predict(self.test_x)
		return hola

	def knn_predict(self):
		neigh = KNeighborsClassifier(n_neighbors=5)
		neigh.fit(self.train_x, self.train_y)
		hola = neigh.predict(self.test_x)
		return hola


def main():
	pred = predict()
	res1 = pred.svm_predict()
	res2 = pred.knn_predict()
	pred.writedown(res1,'results/svmresults.txt')

if __name__ == '__main__':
	main()