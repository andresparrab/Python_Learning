import pandas as pd

world_cup={'Team':['West Indies','West Indies','India','Australia','Pakistan','Sri Lanka','Australia','Australia','Australia','Insia','Australia'],
           'Rank':[7,7,2,1,6,4,1,1,1,2,2],
           'Year':[1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015]
           }
df = pd.DataFrame(world_cup)
#print(df)
# Sort the dataframe by group by groups Team and Rank and it group it for example:
# Australia was in rank number 1 at indexes 3,6,7,8 and the data type int64
print(df.groupby(['Team','Rank']).groups)

#iterates trought the dataframe ans shows the names and the groups that correspont to that name
# example, name is 'Australia and has the groups TEam name, rank and year
for name , groups in df.groupby('Team'):
    print('Group name:', name)
    print(name, groups)
    print('=======================')

# if wee want to just look at a single group we do like this:
print('//////////////////////////////////////////////')
# sort the dataframe by groups ans store it in a variable called grouped
grouped = df.groupby('Team')
# print out the selectec group with get_group
print(grouped.get_group('Australia'))

#or you can write like this in one line, but is prefered to make the code as readable as posible
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print(df.groupby('Team').get_group('Australia'))