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
    if (50< x < 100 and 90< y < 140):
           # print('Stressad', x, y)
            return 1
    else:
       # print('Inte stressad', x, y)
        return 0

training_df = pd.DataFrame()
#z= np.array(range(0,100))
training_df['X']=[]
training_df['Y']=[]
training_df['Stress']=[]
for i in range(1,5000):
    x = np.random.uniform(0,150,1)
    y = np.random.uniform(0, 150,1)
   # print(x)
    x1.append(x)
    y1.append(y)
    stress1.append(getStress(x,y))

training_df['X'] = x1
training_df['Y'] =y1
training_df['Stress'] = stress1
print(training_df.info())


features = training_df.drop('Stress',axis=1)
#print(features)
label= training_df['Stress']
#print(label)
#features = preprocessing.scale(features)
print(features)
#sns.heatmap(training_df.corr())


ax2 = training_df.plot.scatter(x='X',
                      y='Y',
                      c='Stress',
                      colormap='viridis')
plt.show()

# 3. Training the model
features_train,features_test,label_train,label_test = train_test_split(features,label,test_size=0.2,random_state=0)
model = LogisticRegression(random_state=0)
model.fit(features_train,label_train)

# 4. Testing the model: predict and accuracy
stress_predict = model.predict(features_test)

accuracy = model.score(features_test,label_test)
print(confusion_matrix(label_test,stress_predict))
print('The accuracy of the model is :',accuracy*100, '%')

ax3 = features_test.plot.scatter(x='X',
                      y='Y',
                      c=label_test,
                      colormap='viridis')
plt.show()
print(label_test.value_counts())