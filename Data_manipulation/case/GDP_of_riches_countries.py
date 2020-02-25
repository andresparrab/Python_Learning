import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(50,50))
dataset=pd.read_csv('AllCountries.csv')
#print(dataset)
#print(dataset.dtypes)
# Asign only the columns of Country,GDP and BirthRate to selected_dataset
selected_data = dataset.loc[:, ['Country', 'GDP','BirthRate','Internet']]
#print(selected_data)

sorted_data = selected_data.sort_values(by='GDP',ascending=False)
selected_sorted_data =sorted_data.iloc[:10]
print(selected_sorted_data)


plt.pie(selected_sorted_data['GDP'], labels=selected_sorted_data['Country'])

# Show the plot
plt.title('GDP of the ritches couuntries')
plt.show()
