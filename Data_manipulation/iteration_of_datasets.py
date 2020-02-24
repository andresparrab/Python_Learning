import numpy as np
import pandas as pd

df= pd.DataFrame(np.random.rand(5,4),columns=['Col1','Col2','Col3','Col4'])
print(df)

for key,value in df.iteritems():
    print(key, value)