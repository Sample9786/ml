import pandas as p

data=[21,34,56,87,89]

ds=p.Series(data)
print(ds)
ds=ds[2:4]
print('slice\n',ds)