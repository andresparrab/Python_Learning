import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
# 1. Collectinc data
titanic_data = pd.read_csv('titanic.csv')
#print(titanic_data.head)
print(titanic_data.dtypes)
# print(len(titanic_data.index))
# print(titanic_data.count())
#titanic_data.info()


# 2. Analyzing data
# sns.countplot(x='Survived', data=titanic_data)
# plt.show()
#
# sns.countplot(x='Survived', hue='Sex', data=titanic_data)
# plt.show()
#
# sns.countplot(x='Survived', hue='Pclass', data=titanic_data)
# plt.show()
#
# titanic_data['Age'].plot.hist()
# plt.show()
#
# titanic_data['Fare'].plot.hist()
# plt.show()



# 3. Data Wrangling, remove all the unecessary data/colummns  and NaN values
print(titanic_data.isnull().sum())

# sns.heatmap(titanic_data.isnull(),yticklabels=False, cmap='viridis')
# plt.show()
#
#
# sns.boxplot(x='Pclass', y='Age', data=titanic_data)
# plt.show()

print(titanic_data.head(5))
titanic_data.drop('Cabin',axis=1,inplace=True)
print(titanic_data.head(5))
# here we drop all NAN values
titanic_data.dropna(inplace=True)
# we verify that now the data is clean
sns.heatmap(titanic_data.isnull(),yticklabels=False, cmap='viridis')
#plt.show()
# comfirm that there is 0 NAN values
print(titanic_data.isnull().sum())

# get data that is not a number like sex=male or female, and set the value to 1 or 0
# and drop the first column , because we know is male is 0 then is female
print(pd.get_dummies(titanic_data['Sex'],drop_first=True))
#asign to new variable
sex = pd.get_dummies(titanic_data['Sex'],drop_first=True)
print('SEX',sex.dtypes)
# get the dummy data for embarked and drop the first column
embark = pd.get_dummies(titanic_data['Embarked'], drop_first=True)
print(embark)
# get the dummy data for Pclass and drop the first column
pclass = pd.get_dummies(titanic_data['Pclass'], drop_first=True)
print(pclass)
# Now set together/concatinate to set all the new ows and column into one dataset

titanic_data = pd.concat([titanic_data,sex,embark,pclass],axis=1)

# So now we have 5 more columns that have been made in categorical data.
#so we can drop the sex, Embarked and Pclass column that are strings anyway, useless

titanic_data.drop(['Sex','Embarked','PassengerId','Name','Ticket','Pclass'], axis=1,inplace=True)
print(titanic_data)

# 4. TRAIN AND TEST THE DATA
# Train the dataset
X = titanic_data.drop('Survived',axis=1)   # X are the independent variables
y = titanic_data['Survived']            # Y is the dependent variable, it depends of all the features
print('X before processin',X.dtypes)
X = preprocessing.scale(X)

#training the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3 , random_state=1)
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
# Testing the data agains the  .3 or 30% that we saved before
accuracy = logmodel.score(X_test,y_test)
print('The acurracy is :::::::::::::',accuracy)  # accuracy was 0.7710280373831776 ...around 77.1%
predictions = logmodel.predict(X_test)
print(predictions)
print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))
print(accuracy_score(y_test,predictions))