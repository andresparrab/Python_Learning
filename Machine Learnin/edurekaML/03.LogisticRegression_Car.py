import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap

SUV_data = pd.read_csv('SocialNetworkAds.csv')
print(SUV_data)

# 2. Analyzing data
sns.heatmap(SUV_data.corr(),cmap='gnuplot')
plt.show()
SUV_data['Age'].plot.hist()
plt.show()
sns.boxplot(x='Purchased',y='Age', data=SUV_data)
plt.show()
sns.boxplot(x='Gender',y='Purchased', data=SUV_data)
plt.show()

# 3. Data Wrangling, remove all the unecessary data/colummns  and NaN values
X = SUV_data.iloc[:,[2,3]].values
y = SUV_data.iloc[:,4].values
X = preprocessing.scale(X)
# 4. TRAIN AND TEST THE DATA
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=0)

print('X_TEST IS THIS MOTHER FUCKER ::::', X_test)
clf = LogisticRegression(random_state=0)
clf.fit(X_train,y_train)
acc = clf.score(X_test,y_test)

y_pred = clf.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(y_pred)
print(acc)

X_set,y_set = X_test,y_test
print('THE SLICE X_SET S :::::',X_set.iloc[:,0].min())
X1,X2 = np.meshgrid(np.arange(start=X_set.iloc[:,0].min() - 1,stop=X_set.iloc[:,0].max()+1,step=0.01),
                    np.arange(start=X_set.iloc[:,1].min() - 1,stop=X_set.iloc[:,1].max()+1,step=0.01))
plt.contourf(X1,X2,clf.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
                        alpha=0.75,cmap=ListedColormap(('blue','red')))

plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set ==j,0],X_set[y_set == j,1],
               c=ListedColormap(['blue','red'])(i),label=j)

plt.title('Logistic egression (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()