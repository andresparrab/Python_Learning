import numpy as np
import pandas as pd
x= np.array(range(0,21))
y= np.array(range(10,31))

x1 = []
y1= []
stress1 =[]
print(x)
def  getTestdata(x,y):
    # print(item2)
    if (16 < x < 20 and 8 < y < 12):
            print('Stressad', x, y)
            x1.append(x)
            y1.append(y)
            return stress1.append(2)
    else:
        print('Inte stressad', x, y)
        x1.append(x)
        y1.append(y)
        return stress1.append(1)

getTestdata(17,9)
getTestdata(15,9)
getTestdata(15,97)
getTestdata(2,3)
df = pd.DataFrame()
df['X'] = x1
df['Y'] =y1
df['Stress'] = stress1
print(df)