import pandas as pd

data=pd.read_csv('titanic.csv')

print(data.head())

print('Data information\n')

print(data.describe())

print('DataType \n')
print(data.info())