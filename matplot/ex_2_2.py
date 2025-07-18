import pandas as pd

data=pd.read_csv('titanic.csv')

data.drop(['SibSp','Parch'],axis=1,inplace=True)
print(data.head())

data['Age']=data['Age'].fillna(data['Age'].median())

print(data.head())
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

print('Final \n')
print(data.isnull().sum())
