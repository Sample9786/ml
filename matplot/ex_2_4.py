import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data=pd.read_csv('titanic.csv')


plt.figure(figsize=(13, 10))

plt.subplot(2, 3, 1)
sns.histplot(data['Age'],color='skyblue')
plt.title('Distribution of Age')

plt.subplot(2, 3, 2)
sns.countplot(x='Sex', data=data, palette='Set2')
plt.title('Count by Gender')

plt.subplot(2, 3, 3)
sns.barplot(x='Sex', y='Survived', data=data, palette='Set2')
plt.title('Survival Rate by Gender')

plt.subplot(2, 3, 4)
sns.barplot(x='Pclass', y='Survived', data=data, palette='Set2')
plt.title('Survival by Class')

plt.subplot(2, 3, 5)
sns.barplot(x='Survived', y='Age', data=data, palette='Set2')
plt.title('Age vs Survival')

plt.tight_layout()
plt.show()