import pandas as pd
import quandl
quandl.ApiConfig.api_key = "gwFVwtxy45S5ixw9LPtU"
pd.set_option('display.max_columns', 13)
df = quandl.get("WIKI/GOOGL")

#print(df.head(10))
# grab the relevant features thatwe need from teh DB
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]

df['HL_PCT'] = (df['Adj. High']- df['Adj. Low']) / df['Adj. Close'] * 100
df['PCT_change'] = (df['Adj. Close']- df['Adj. Open']) / df['Adj. Open'] * 100

df = df[['Adj. Close','HL_PCT','PCT_change']]

print(df.tail(50))