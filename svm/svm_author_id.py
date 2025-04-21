#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import numpy as np
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
def SVMAccuracy(features_train, labels_train, features_test, labels_test):
    from sklearn import svm
    from sklearn.metrics import accuracy_score
    # Initialize the SVM classifier with an rbf kernel
    clf = svm.SVC(kernel='rbf', C=10000.0)

    #clf = svm.SVC(kernel='linear')

    # reduce the training set size for faster execution
    #features_train = features_train[:len(features_train)/100]
    #labels_train = labels_train[:len(labels_train)/100]

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

    #print("Prediction for 10th email:", pred[10])
    #print("Prediction for 26th email:", pred[26])
    #print("Prediction for 50th email:", pred[50])

    # print total number of predicted Chris and Sara emails.
    print("Number of Chris emails:", np.sum(pred == 1))
    print("Number of Sara emails:", np.sum(pred == 0))
    # Calculate the accuracy of the predictions
    accuracy = accuracy_score(labels_test, pred)
    return accuracy                                                                                 
#########################################################


# Call the function and print the accuracy                      
accuracy = SVMAccuracy(features_train, labels_train, features_test, labels_test)
print("NB Accuracy:", accuracy)

