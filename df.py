import pandas as p
import numpy as np
data={
    'name':['mano','jai','krish','ram'],
    'profession':['student','baby','second baby','mechanic'],
    'age':[21,5,6,35]
}

df=p.DataFrame(data)

print(df)
score={
    'score':[65,87,54,78]
}
df2=p.DataFrame(score)
df=df.join(df2)

df['status']=np.where(df['score']<60,'Fail','Pass')         #used numpy
df['Age_Restriction']=df['age'].apply(lambda x:'less' if x<18 else 'high')  #used pandas
print(df)
df.to_csv('df.csv')