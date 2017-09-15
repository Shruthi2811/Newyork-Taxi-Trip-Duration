# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:08:24 2017

@author: Administrator
"""

import pandas as pd
train = pd.read_csv('S:\Kaggle\Taxi Duration\train\train.csv')
#test = pd.read_csv('Data/test.zip', compression='zip',parse_dates=['pickup_datetime'])
print(train.head())
print(train.info())