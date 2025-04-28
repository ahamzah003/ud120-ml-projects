#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(grade_fast, bumpy_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("grade")
plt.ylabel("bumpiness")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

def KNNAccuracy(features_train, labels_train, features_test, labels_test):
    from sklearn.neighbors import KNeighborsClassifier
    # n_neighbors = 7; determined using sq. root of training set size=750
    KNNclf = KNeighborsClassifier(n_neighbors=7, p=2, metric='minkowski')
    print("n_neighbors = 7\n")

    scaler = MinMaxScaler()
    features_train_scaled = scaler.fit_transform(features_train)
    features_test_scaled = scaler.transform(features_test)

    # set start time to measure training time
    t0 = time()
    # Fit the classifier to the training data
    KNNclf.fit(features_train_scaled, labels_train)
    # set end time to measure training time
    print "training time:", round(time()-t0, 3), "s"

    # set start time to measure prediction time
    t0 = time()
    # Predict the labels for the test data
    pred = KNNclf.predict(features_test_scaled)
    # set end time to measure prediction time
    print "predicting time:", round(time()-t0, 3), "s"

    # Calculate the accuracy of the predictions
    accuracy = accuracy_score(labels_test, pred)
    return accuracy, KNNclf, features_test_scaled



# Call the function and print the accuracy                      
accuracy, KNNclf, features_test_scaled  = KNNAccuracy(features_train, labels_train, features_test, labels_test)
print("KNN Accuracy:", accuracy)

try:
    prettyPicture(KNNclf, features_test_scaled, labels_test)
except NameError:
    pass





