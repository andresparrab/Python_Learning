import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

plt.figure(figsize=(50,50))
dataset = pd.read_csv('heart_rate_edited.csv')

print(dataset.dtypes)
print(dataset.describe())

selected_data = dataset.loc[:,['HR','ElapsedTime']]
print(selected_data)
x = np.array(selected_data['ElapsedTime'])
y= np.array(selected_data['HR'])

plt.plot(x,y)
plt.title('Relations betwen Heart Rate and Time Elapsed')
plt.ylabel('Heart Rate')
plt.xlabel('ElapsedTime')
plt.show()