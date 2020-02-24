import pandas as pd
import numpy as np

#df=pd.Series(np.arange(1,51))
df= pd.DataFrame({'a': pd.Series(np.arange(1,51)),'b': pd.Series(np.arange(51,101))})
print(df.values)
print(df.ndim)
print(df.axes)
# heads will give you first five rows, is good if you have hundreds of thousand of rows
# then you can print the first five by default or 10 or 15 etc to see just how they work
print(df.head())
#tail print the last rows
print(df.tail())
#print(np.arange(1,50))