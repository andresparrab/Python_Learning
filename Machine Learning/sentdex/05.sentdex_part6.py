import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import  preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')



quandl.ApiConfig.api_key = "gwFVwtxy45S5ixw9LPtU"
pd.set_option('display.max_columns', 13)
df = quandl.get("WIKI/GOOGL")

#print(df.head(10))
# grab the relevant features that we need from teh DB
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High']- df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close']- df['Adj. Open']) / df['Adj. Open'] * 100.0
#            PRICE        X       X            X
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
#print(df.head())

# Start the regression algorithm
forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

# math.ceil will round up to a whole number , if the len of df is 22
# and the 1 the 10% is 0.1*22= 2.2 it will round up to 3
# then change to int at the end instead of 2.0
forecast_out =int(math.ceil(0.1*len(df))) # we try to predict 1%=35 days of the data frame
#print(forecast_out)
# in the column label it will take the row of forecast_col and shift insert with the last value of
# forecast out that is 1% into the future
df['label'] = df[forecast_col].shift(-forecast_out) # the 'label' column will have the Adj. Close price 1%.. is 35 days in advance into the future
#df.dropna(inplace=True) # this will drop the whole row if have NaN values
#print(df.tail(20))
#print(df.head(20))

# Capital X are the features
X = np.array(df.drop(['label'],1)) # the features has to be everything except the label column ",1" is for columns

# Scale the features
X = preprocessing.scale(X) # maybe less good to use in real time data
X_lately = X[-forecast_out:] #all the   x from -forecast out to the end. in this case the last 35
X = X[:-forecast_out] # all the x values will be until the last value of forecast_out

# lowercase y are the labes
#y = np.array(df['label'])

df.dropna(inplace=True)
y = np.array(df['label'])
#y = np.array(df['label'])
#print(len(X),len(y))

# we are creating our training and testing set

# 20% of the data are be going to be used as testing data, it shuffles everything upp
X_train, X_test, y_train,y_test = model_selection.train_test_split(X,y,test_size=0.2)

# Using Linear Regression algorithm
#clf = LinearRegression(n_jobs=-1) # n_jobs = -1 use as many jobs  as possible the processor can handle
# Shifting to Svm= support vector machine algorithm
#clf = svm.SVR() # In this case is much less accurate
# clf.fit takes X_train as features and y_train as LABELS
#clf.fit(X_train,y_train)
#now we have a trained clasifier that we can save for later use
#in thiscase we will save it in file linearregression.pickle,and assign to variable f
#with open('linearregression.pickle', 'wb') as f:
#    pickle.dump(clf, f)

# For use the pickle just write this
pickle_in = open('linearregression.pickle', 'rb')
clf = pickle.load(pickle_in)

#clf score TEST the data and we can see the accuracy
accuracy =  clf.score(X_test,y_test)

#print(accuracy)
# predicting the unknown future data
forecast_set = clf.predict(X_lately) #making a clasifier that will predict based on the X data
print(forecast_set, accuracy, forecast_out)


df['Forecast'] = np.nan #createthe last column ame Forecast


last_date = df.iloc[-1].name
print('The last_date = df.iloc[-1].name is ::::::::::::::::::: ', last_date)
last_unix = last_date.timestamp()
print('timestamp is /////////////////  ', last_unix)
one_day = 86400
next_unix= last_unix + one_day

print(df.tail(40))
for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    #df.loc[next_date] this say if next date not exist create it , if exist, replace it with next_date
    #[np.nan for _ in range (len(df.columns)-1)]+ [i]    this mean all exept the last column fill with NaN
    # and to the last column insert the value of i. that is the Forecast values
    df.loc[next_date] = [np.nan for _ in range (len(df.columns)-1)]+ [i]

print(df.tail(40))


df['Adj. Close'].plot() #plot the graph1 with the Adj,Close prices
df['Forecast'].plot() # plot the second graph with the future predictions
plt.legend(loc=4)  #set the legend inlocation 4,down to the right
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()