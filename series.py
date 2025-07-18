import pandas as pd

player_list = [['M.S.Dhoni', 36, 75, 5428000],
               ['A.B.D Villers', 38, 74, 3428000],
               ['V.Kohli', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000],
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]

df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])
print(df)

# slicing rows
df1 = df.iloc[0:4]
print(df1)

#slicing colums
df1 = df.iloc[:, 0:2]
print(df1)

#using conditions for slicing
data = df[df['Age'] > 35].iloc[:, :] 
print("\nFiltered Data based on Age > 35:\n", data)

#using loc() for slicing rows
df.set_index('Name', inplace=True)
custom = df.loc['A.B.D Villers':'S.Smith']
print(custom)
