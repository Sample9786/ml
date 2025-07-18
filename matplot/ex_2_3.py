import pandas as pd

data=pd.read_csv('titanic.csv')
print('data Mean :\n',data['Age'].mean())
print('data Median :\n',data['Age'].median())
print('data Mode :\n',data['Age'].mode())
print('count :\n',data.groupby('Sex').size())
print('count :\n',data.groupby('Pclass').size())
print('count :\n',data.groupby('Survived').size())

print('using count operation :\n',data['Sex'].value_counts())