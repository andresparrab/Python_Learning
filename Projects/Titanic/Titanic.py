import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import math

original_df = pd.read_csv('titanic.csv')

print('# of passenger s in the original data:'+ str(len(original_df.index)) + '\n')

print(original_df.head())
print(original_df.dtypes)

# Prints the number of passengers that have NaN in each column
print(original_df.isnull().sum())

age_wrangled_df = original_df[pd.notnull(original_df['Age'])]
print('# of passengers in age wrangled data : ' +str(len(age_wrangled_df.index))+ '\n')

embark_wrangled_df = age_wrangled_df[pd.notnull(age_wrangled_df['Embarked'])]
print('# of passengers in age & embark wrangled data: '+ str(len(embark_wrangled_df.index)) + '\n')

# Now we will group data by gender
gender_data =embark_wrangled_df.groupby('Sex', as_index=False)
gender_mean_data = gender_data.mean()

print('Total Survival Rate: ' + str(embark_wrangled_df['Survived'].mean()))
print('\nMean Data by Gender')
print(gender_mean_data[['Sex','Survived','Age','Pclass','SibSp','Parch','Fare']])

# prints the  total number of passengers survived  sorted by sex
print('==========================================')
total_df = gender_data['PassengerId'].count()
print(total_df)

# Rename the PassengerId  column to the label total
print('-------------------------------------')
total_df.columns = ['Sex', 'Total']
print(total_df)

gender_list = total_df['Sex'] # saves the 'Sex' column in another list for later use in plot

del total_df['Sex']
print('.......................................')
print( total_df)
print(gender_data)

#Find number of male and females tat survived

gender_survived_df = gender_data['Survived'].sum()
print(gender_survived_df)
del gender_survived_df['Sex']
print(gender_survived_df)

#combine series using vectorized operations
combined_df = total_df.add(gender_survived_df, fill_value = 0)
print(combined_df)

# now we will plot
combined_df.plot.bar(color=['limegreen','dodgerblue'])
plt.title('Effect of gender survival')
plt.xlabel('Gender')
plt.ylabel('# of people')
plt.xticks(range(len(gender_list)),gender_list)
print('::::::::::::::::::::::::::::::::::::')
print(len(gender_list))
print(gender_list)

survival_gender_list = [combined_df.loc[0]['Survived'], combined_df.loc[1]['Survived']]
total_gender_list = [combined_df.loc[0]['Total'], combined_df.loc[1]['Total']]

# Define a function to create value labels on plots
def create_value_labels(list_data, decimals, x_adjust, y_adjust):
    for x,y in enumerate(list_data):
        plt.text(x + x_adjust, y + y_adjust, round(list_data[x], decimals), color='w', fontweight='bold')

create_value_labels(survival_gender_list, 1, -0.2, -50)
create_value_labels(total_gender_list, 1, 0.05, -50)
plt.show()