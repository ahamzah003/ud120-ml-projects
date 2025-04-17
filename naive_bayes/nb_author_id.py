#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
def NBAccuracy(features_train, labels_train, features_test, labels_test):
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    # Initialize the Gaussian Naive Bayes classifier                            
    clf = GaussianNB()
    # set start time to measure training time
    t0 = time()
    # Fit the classifier to the training data
    clf.fit(features_train, labels_train)
    # set end time to measure training time
    print "training time:", round(time()-t0, 3), "s"
    # set start time to measure prediction time
    t0 = time()
    # Predict the labels for the test data
    pred = clf.predict(features_test)
    # set end time to measure prediction time
    print "predicting time:", round(time()-t0, 3), "s"
    # Calculate the accuracy of the predictions
    accuracy = accuracy_score(labels_test, pred)
    return accuracy


# Call the function and print the accuracy                      
accuracy = NBAccuracy(features_train, labels_train, features_test, labels_test)
print("NB Accuracy:", accuracy)
#########################################################


