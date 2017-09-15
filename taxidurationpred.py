# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:08:24 2017

@author: Shruthi Ramakrishnan
"""
#Reading train and test dataset
import pandas as pd
train = pd.read_csv('S:\\Kaggle\\Taxi\\train\\train.csv')
test = pd.read_csv('S:\\Kaggle\\Taxi\\test\\test.csv')

#removind the dropoff time and trip duration from the dataset
train_new = train.drop('trip_duration',1)
train_new = train_new.drop('dropoff_datetime',1)
predictedvalue = train['trip_duration']
dropof_training = train['dropoff_datetime']

#merge train and test dataset for data cleaning
merged_data = [train_new , test] 
finaldata = pd.concat(merged_data)
