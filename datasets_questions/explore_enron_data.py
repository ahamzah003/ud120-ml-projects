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


# Module 6.16
# how many POIs exist
with open("../final_project/poi_names.txt", "r") as f:
    lines = f.readlines()

# skip the first two lines (header and blank line)
poi_names = [line.strip() for line in lines[2:]]
print("Total Number of POIs in the poi_names.txt file: ", len(poi_names))



# get the number of POIs with a "y" in the poi_names.txt file
y_count = 0
for poi_name in poi_names:
    if poi_name[1]=="y":
        y_count+=1
    else:
        continue    

print("Number of Yes-POIs in the poi_names.txt file: ", y_count)


# get POIs names and print the names of all features
persons = [person.strip() for person in enron_data.keys()]
feature_names = enron_data[persons[0]]
print(feature_names)


# define a function to search for a POI name matching a string
def reSearch(search_string, string, case_ignore=True):
    """
    This function takes a search string and a string to search for
    and returns True if the search string is found in the string,
    otherwise it returns False.
    """
    import re
    flags = re.IGNORECASE if case_ignore else 0
    if re.search(search_string, string, flags=flags):
        print(string)
        return True
    else:
        return False
    


# Module 6.18
# query the dataset 1 - What is the total value of the stock belonging to James Prentice?
# search for James Prentice in the dataset
for person in persons:
    reSearch("james", person)

# print the total value of stocks belonging to James Prentice
print("Total value of stocks belonging to James Prentice: ", enron_data["PRENTICE JAMES"]["total_stock_value"])
print("\n")



# Module 6.19
# query the dataset 2 - How many email messages do we have from Wesley Colwell to persons of interest?

# search for Wesley Colwell in the dataset
for person in persons:
    reSearch("colwell", person)

print("Number of emails from Wesley Colwell to POIs: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print("\n")
