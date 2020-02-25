import pandas as pd

df= pd.read_csv('Volcanoes_USA.txt')
lon=list(df['LON'])
lat=list(df['LAT'])
elev=list(df['ELEV'])
print(lon)
print(lat)
print(elev)
print(df.dtypes)