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



# Module 6.20
# query the dataset 3 - What is the value of stock options exercised by Jeffrey Skilling?

# search for Jeffrey Skilling in the dataset
for person in persons:
    reSearch("skilling", person)

print("Value of stock options exercised by Jeffrey Skilling: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
print("\n")



def getMostPaid(p_dict):
    """
    This function takes a dictionary of features 
    and returns the name of the person with the 
    highest total payments in the Enron dataset.
    """
    for poi in p_dict.keys():
        total_payment = enron_data[poi]["total_payments"]
        p_dict[poi] = total_payment
    # get maximum of the key-value tuples of `p_dict.items()` 
    # using the value as the key parameter for `max()`
    exco = max(p_dict.items(), key=lambda x: x[1])
    print("{} took home the most money: ${}\n".format(exco[0], exco[1]))



# Module 6.25
# Of there three individuals (Lay, Skilling, and Fastow),
# who took home the most money?
poi_list = ["LAY KENNETH L", "SKILLING JEFFREY K", "FASTOW ANDREW S"]
poi_dict = dict.fromkeys(poi_list)
getMostPaid(poi_dict)



# Module 6.27a
# How many people in the dataset have a quantified salary?

sal_n = 0
# a for-loop to iterate through the persons in the dataset
# and check if the salary is not "NaN"
for person in persons:
    if enron_data[person]["salary"] != "NaN":
        sal_n += 1

print "{} people have a quantified salary".format(sal_n)

# Module 6.27b
# How many people in the dataset have a known email address?

email_n = 0

for person in persons:    
    if enron_data[person]["email_address"] != "NaN":
        email_n += 1

print "{} people have a known email address".format(email_n)



# Module 6.29
# dict-to-array conversion
# What percentage of people in the dataset have "NaN" for their total payments?

feature_list = ["poi","total_payments"]
# NaNs are by default converted to zeros in the featureFormat function,
# so we need to set remove_NaN=True and remove_all_zeroes=True to remove them from the array. 
arr = featureFormat(enron_data, feature_list,remove_NaN=True, remove_all_zeroes=True)
# subtract the number of rows in the array from the total number of people in the dataset
# to get the number of people with NaN for total payments   
tp_nan = len(enron_data) - arr.shape[0]
# print the number of people with NaN for total payments
print "\n{} people in the E+F dataset have 'NaN' for their total payments.\n".format(tp_nan)
# print the percentage of people with NaN for total payments
print "That makes {}% of the total people in the dataset".format(round((float(tp_nan)/float(len(enron_data)))*100, 2))
