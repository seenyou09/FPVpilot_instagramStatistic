#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 15:55:01 2023

@author: seanyoo
"""
import pandas as pd
import json 
from insta_stats import insta_stats

# Read the CSV file into a DataFrame
pilot_df = pd.read_csv('/Users/seanyoo/Desktop/insta_statistic_project/csv/centralPilotdf.csv')


#convert to Json file
insta_list = pilot_df['Instagram'].values.tolist()
filename = "insta_info.json"
i= 0 
for url in insta_list:
    try:
        trial = insta_stats(url)
        trial.updateJson(filename)
    except:
        pass
       

filename = "insta_info.json"
with open(filename) as file:
    # Load the JSON data
    data = json.load(file)

df = pd.DataFrame(data)
df2 = df.T
df2

#Convert to Excel File
df2.to_excel(r'/Users/seanyoo/Desktop/insta_statistic_project/insta_info.xlsx', index=False)
