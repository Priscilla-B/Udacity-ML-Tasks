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

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))


print('number of data points: ', len(enron_data))
sample_data_point = enron_data[list(enron_data.keys())[0]]
print('number of features: ', len(sample_data_point.keys()))

# how many POIs?
poi_names = open("../final_project/poi_names.txt", 'r')
next(poi_names)
next(poi_names)
print('Number of POIs', (len(poi_names.readlines())))
poi_names.close()

# how many emails from Wesley Colwell to POI?
print('emails from Wesley Colwell to POIs: ', enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

# value of stock options exercised by Jeffrey K Skilling
print('value of stock options Jeffrey:', enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

# how many people have a quantified salary?
salary_list = []
for key in enron_data.keys():
    salary_list.append(enron_data[key]['salary'])
print('number of people with a quantified salary', len(salary_list) - salary_list.count('NaN'))

# number of people with a know email address
email_list = []
for key in enron_data.keys():
    email_list.append(enron_data[key]['email_address'])
print('number of people with a known email', len(email_list) - email_list.count('NaN'))

