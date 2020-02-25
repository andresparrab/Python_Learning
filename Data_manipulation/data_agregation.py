import pandas as pd
import numpy as np

d= {'odd': np.arange(1,100,2), 'even': np.arange(0,100,2)}
print(d['odd'])
print(d['even'])

df=pd.DataFrame(d)
# An aggregated function returns a single aggregated value for each group
# example, sum all the values in the group odd and return the total sum
# or in this case return a single roud showing the value of the odd number,index stored and dtype
print(df.groupby('odd').groups)
# print the sum
print(sum(df.groupby('odd').groups))

