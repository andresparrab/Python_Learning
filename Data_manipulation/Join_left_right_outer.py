import pandas as pd

world_cup={'Team':['West Indies','India','Australia','Pakistan','Sri Lanka'],
           'Rank':[7,7,2,1,6],
           'Year':[1975,1979,1983,1987,1992],
           'Points':[956,876,786,699,744]
           }
chockers ={
    'Team':['South Africa','New Zeeland','Zimbawua'],
    'Rank':[1,5,9],
    'Points':[895,786,654]}


df_wolrd_cup = pd.DataFrame(world_cup)
df_chockers = pd.DataFrame(chockers)

print(pd.merge(df_wolrd_cup,df_chockers, on='Team', how='left'))
print('--------------------------------------------------------')
print(pd.merge(df_wolrd_cup,df_chockers, on='Team', how='right'))
print('--------------------------------------------------------')
print(pd.merge(df_wolrd_cup,df_chockers, on='Team', how='outer'))
print('--------------------------------------------------------')
print(pd.merge(df_wolrd_cup,df_chockers, on='Team', how='inner'))