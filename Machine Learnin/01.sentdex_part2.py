import pandas as pd
import quandl
quandl.ApiConfig.api_key = "gwFVwtxy45S5ixw9LPtU"
pd.set_option('display.max_columns', 13)
df = quandl.get("WIKI/GOOGL")

print(df.head(10))

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]