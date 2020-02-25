import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(50,50))
dataset=pd.read_csv('AllCountries.csv')
#print(dataset)
#print(dataset.dtypes)
# Asign only the columns of Country,GDP and BirthRate to selected_dataset
selected_data = dataset.loc[:, ['Country', 'GDP','BirthRate']]
#print(selected_data)
sorted_data = selected_data.sort_index(by='Country', ascending=False)
#selected_sorted_data =sorted_data.iloc[:10]
#print(selected_sorted_data)

# Asign the values of the GDP to x for ploting later
#x = np.array(selected_data['GDP'])
# Asign the values of BirthRate to y for ploting later
#y = np.array(selected_data['BirthRate'])
# Make the scater function wuth the GDP and BirthRate
#plt.scatter(x,y)
# limit the x axis to 20000
#plt.xlim(0,20000)
# Show the plot
#plt.title('Relations betwen GDP and BirthRate')
#plt.xlabel('GDP')
#plt.ylabel('BirthRate')
#plt.show()
#print(selected_data['Country'][3])