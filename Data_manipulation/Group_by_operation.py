import pandas as pd

world_cup={'Team':['West Indies','West Indies','India','Australia','Pakistan','Sri Lanka','Australia','Australia','Australia','Insia','Australia'],
           'Rank':[7,7,2,1,6,4,1,1,1,2,2],
           'Year':[1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015]
           }
df = pd.DataFrame(world_cup)
print(df)
print(df.groupby(['Team','Rank']).groups)

for name , groups in df.groupby('Team'):
    print(name, groups)
    print('=======================')