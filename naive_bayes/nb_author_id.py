#!/usr/bin/python

import sys
from time import time
import pandas as pd
from pandas import DataFrame
import sklearn
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
sys.path.append("../tools/")
from email_preprocess import preprocess

# features_train and features_test are the features for the training
# and testing datasets, respectivelyfrom sklearn.Naive_Bayes import GaussianNB
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print('training time:', round(time()-t0, 3), "s")
t1 = time()
pred = clf.predict(features_test)
print('testing time:', round(time()-t1, 3), "s")
#print(pred)

accuracy = accuracy_score(pred, labels_test)
print(accuracy)




"""number_of_emails = len(labels_train)
count_of_Chris = sum(labels_train)
count_of_Sarah = number_of_emails - sum(labels_train)

prob_Chris = count_of_Chris/number_of_emails
prob_Sarah = 1-prob_Chris

print(prob_Chris, prob_Sarah)
print(features_train)
features_train_df = DataFrame(features_train)
print(features_train_df)
print(features_train_df.value_counts())
"""


