#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

"""
from sklearn.svm import SVC
clf = SVC(kernel='linear')
t0 = time()
clf.fit(features_train, labels_train)
print('training time:', round(time()-t0, 3), "s")

t1 = time()
pred = clf.predict(features_test)
print('testing time:', round(time()-t1, 3), "s")

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)

print(accuracy)
"""

# with smaller training data
features_train = features_train[:len(features_train)//100]
labels_train = labels_train[:len(labels_train)//100]


from sklearn.svm import SVC
clf = SVC(C=10, kernel='rbf')
t0 = time()
clf.fit(features_train, labels_train)
print('training time:', round(time()-t0, 3), "s")

t1 = time()
pred = clf.predict(features_test)
print('testing time:', round(time()-t1, 3), "s")

print('Pred 10th:', clf.predict(features_test[10].reshape(1, -1)))
print('Pred 26th:', clf.predict(features_test[26].reshape(1, -1)))
print('Pred 50th:', clf.predict(features_test[50].reshape(1, -1)))

import numpy as np
values, counts = np.unique(pred, return_counts=True)
print(values, counts)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)

print(accuracy)

# C=10: accuracy = 0.8999
# C=100: 0.8999
