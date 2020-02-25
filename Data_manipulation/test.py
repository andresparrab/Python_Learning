import pandas as pd

world_cup={'Team':['West Indies','India','Australia','Pakistan','Sri Lanka'],
           'Rank':[7,7,2,1,6],
           'Year':[1975,1979,1983,1987,1992],
           'Points':[956,876,786,699,744]
           }
chockers ={
    'Team':['West Indies','India','Australia','Pakistan','Sri Lanka'],
    'cup_played':[11,15,19,2,7],
    'ODIS played':[895,786,766,544,643]}


df_wolrd_cup = pd.DataFrame(world_cup)
df_chockers = pd.DataFrame(chockers)
#print(df_chockers)
print(pd.merge(df_wolrd_cup,df_chockers, on='Team'))