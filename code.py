import pandas as pd
train = pd.read_csv('Data/train.zip', compression='zip',parse_dates=['pickup_datetime','dropoff_datetime'])
test = pd.read_csv('Data/test.zip', compression='zip',parse_dates=['pickup_datetime'])
print(train.head())
print(train.info())
