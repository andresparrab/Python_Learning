import pandas as pd
import quandl, math
import numpy as np
from sklearn import  preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

quandl.ApiConfig.api_key = "gwFVwtxy45S5ixw9LPtU"
pd.set_option('display.max_columns', 13)
df = quandl.get("WIKI/GOOGL")

#print(df.head(10))
# grab the relevant features that we need from teh DB
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High']- df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close']- df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
#print(df.head())

# Start the regression algorithm
forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

# math.ceil will round up to a whole number , if the len of df is 22
# and the 1 the 10% is 0.1*22= 2.2 it will round up to 3
# then change to int at the end instead of 2.0
forecast_out =int(math.ceil(0.01*len(df))) # we try to predict 1% of the data frame
print(forecast_out)
# in the column label it will take the row of forecast_col and shift insert with the last value of
# forecast out that is 1% into the future
df['label'] = df[forecast_col].shift((-forecast_out)) # the label column will have the Adj. Close price 1%.. is 35 days in advance into the future
df.dropna(inplace=True)
print(df.tail(20))

print(df.head(20))

# Capital X are the features
X = np.array(df.drop(['label'],1)) # the features has to be everything except the label column
# lowercase y are the labes
y = np.array(df['label'])

# Scale the features
X =  preprocessing.scale(X) # maybe less good to use in real time data
#y = np.array(df['label'])
print(len(X),len(y))

# we are creating our training and testing set

# 20% of the data are be going to be used as testing data
X_train, X_test, y_train,y_test = model_selection.train_test_split(X,y,test_size=0.2)

# Using Linear Regression algorithm
clf = LinearRegression(n_jobs=-1) # n_jobs = -1 use as many jobs  as possible the processor can handle
# Shifting to Svm= support vector machine algorithm
#clf = svm.SVR() # In this case is much less accurate
clf.fit(X_train,y_train)
accuracy =  clf.score(X_test,y_test)

print(accuracy)