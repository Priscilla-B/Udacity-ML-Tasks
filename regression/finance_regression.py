#!/usr/bin/python

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""    


import sys
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load(open("../final_project/final_project_dataset_modified_unix.pkl", "rb"))

#  list the features you want to look at--first item in the
#  list will be the "target" feature
features_list = ["bonus", "salary"]
data = featureFormat(dictionary, features_list, remove_any_zeroes=True,
                     sort_keys='../tools/python2_lesson06_keys_unix.pkl')
target, features = targetFeatureSplit(data)

#  training-testing split needed in regression, just like classification

feature_train, feature_test, target_train, target_test = train_test_split(
    features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"


reg = LinearRegression()
reg.fit(feature_train, target_train)
print('slope:', reg.coef_)
print('intercept:', reg.intercept_)
print('score on training data:', reg.score(feature_train, target_train))
print('score on test data:', reg.score(feature_test, target_test))


# draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

# labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")

# draw the regression line, once it's coded
try:
    plt.plot(feature_test, reg.predict(feature_test))
except NameError:
    pass
reg.fit(feature_test, target_test)
print('slope of new line', reg.coef_)
plt.plot(feature_train, reg.predict(feature_train), color="b")
plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()

# regression of bonus against long-term incentive feature

features_list = ["bonus", "long_term_incentive"]
data = featureFormat(dictionary, features_list, remove_any_zeroes=True,
                     sort_keys='../tools/python2_lesson06_keys_unix.pkl')
target, features = targetFeatureSplit(data)

#  training-testing split needed in regression, just like classification

feature_train, feature_test, target_train, target_test = train_test_split(
    features, target, test_size=0.5, random_state=42)
reg = LinearRegression()
reg.fit(feature_train, target_train)
print('metrics for new regression')
print('slope:', reg.coef_)
print('intercept:', reg.intercept_)
print('score on training data:', reg.score(feature_train, target_train))
print('score on test data:', reg.score(feature_test, target_test))