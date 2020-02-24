import pandas as pd
import numpy as np
d = {'even': np.arange(1, 100, 2),
     'odd': np.arange(0, 100, 2)
     }

print(d['even'])
print(d['odd'])

# convert the dictionary to a dataframe

df = pd.DataFrame(d)
print(df)
# Sum the items in the dataframe from each column
print(df.sum())

# standar deviation
print(df.std())
