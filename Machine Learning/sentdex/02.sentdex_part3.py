import pandas as pd
import quandl
import math

quandl.ApiConfig.api_key = "gwFVwtxy45S5ixw9LPtU"
pd.set_option('display.max_columns', 13)
df = quandl.get("WIKI/GOOGL")

#print(df.head(10))
# grab the relevant features that we need from teh DB
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]

df['HL_PCT'] = (df['Adj. High']- df['Adj. Low']) / df['Adj. Close'] * 100
df['PCT_change'] = (df['Adj. Close']- df['Adj. Open']) / df['Adj. Open'] * 100

df = df[['Adj. Close','HL_PCT','PCT_change']]
print(df.tail(40))

# Start the regression algorithm
forecast_col = 'Adj. Close'
df.fillna('-99999', inplace=True)

# math.ceil will round up to a whole number , if the len of df is 22
# and the 1 the 10% is 0.1*22= 2.2 it will round up to 3
# then change to int at the end instead of 2.0
forecast_out =int(math.ceil(0.01*len(df))) # we try to predict 1% of the data frame
print('forecast:\n', forecast_out)
# in the column label it will take the row of forecast_col and shift insert with the last value of
# forecast out that is 1% into the future
df['label'] = df[forecast_col].shift((-forecast_out)) # the label column will have the Adj. Close price 1% days into the future
df.dropna(inplace=True)
print(df.tail(40))