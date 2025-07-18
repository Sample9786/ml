import pandas as py

df=py.read_csv('sample.csv')
print(df.head())

print('Units Format in Rupees :\n')
print(df[df['UNITS']=='rupees'])

desc=df.describe()
print(desc)

print('Period before 2000s\n')
new=df[df['Period']<=2000]

new.to_csv('updated.csv')
