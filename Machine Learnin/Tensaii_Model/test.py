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
    if (40< x < 80 and 80< y < 100):
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
for i in range(1,50000):
    x = random.uniform(0,150)
    y = random.uniform(0, 150)
   # print(x)
    x1.append(x)
    y1.append(y)
    stress1.append(getStress(x,y))


training_df['X'] = x1
training_df['Y'] =y1
training_df['Stress'] = stress1
print(training_df)

training_df.to_csv('stress.csv',index=False)
print(training_df.count())
print(training_df['Stress'].value_counts())