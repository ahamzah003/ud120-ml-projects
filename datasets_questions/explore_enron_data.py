#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


# Module 6.13
# size of the enron dataset
print("Number of people in the dataset: ", len(enron_data))


# Module 6.14
# features in the enron dataset 
print("Number of features for each person: ",len(next(iter(enron_data.values()))))


# Module 6.15
# finding POIs in the enron dataset
register = 0
for person in enron_data.keys():
    if enron_data[person]['poi']==1:
        register+=1
    else:
        continue

print("Number of POIs in the dataset: ", register)