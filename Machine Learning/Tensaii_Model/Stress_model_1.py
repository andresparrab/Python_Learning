import numpy as np
import pandas as pd
import random
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
x1 = []
y1= []
stress1 =[]

def  getStress(x,y):
    if (50< x < 80 and 90< y < 110):
           # print('Stressad', x, y)
            return 1
    else:
       # print('Inte stressad', x, y)
        return 0

training_df = pd.DataFrame()
training_df['X']=[]
training_df['Y']=[]
training_df['Stress']=[]
#print(training_df)
for i in range(1,5000):
    x = random.uniform(0,150)
    y = random.uniform(0, 150)
    training_df.append
    training_df.append({'Y':y},ignore_index=True)
   # print(x)
   #  x1.append(x)
   #  y1.append(y)
    stress1.append(getStress(x,y))


# training_df['X'] = x1
# training_df['Y'] =y1
training_df['Stress'] = stress1
print(training_df)

training_df.to_csv('stress.csv',index=False)
print(training_df.count())
print(training_df['Stress'].value_counts())