import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyodbc
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
# Parameters
server = 'localhost,1420'
#server = 'cmra_db,1433'
db= 'CMRADatabase'
password = 'Cmra1234'
data_length = '2000'
# Create the connection for runnning outside the container
conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.4.so.2.1};SERVER=' + server +';DATABASE=' +db + ';UID=sa;PWD=' + password)
# SQL Query
sql_sensorData ='SELECT top (' + data_length + ') * FROM sensordata.HeartRate'
#sql_sensorData ='SELECT top (' + data_length + ') * FROM sensordata.HeartRate order by TimeStamp desc'
#sql_eye_data='SELECT top (' + data_length + ') * FROM sensordata.EyeData order by TimeStamp desc'
#sql_head_data='SELECT top (' + data_length + ') * FROM sensordata.Head order by TimeStamp desc'



# Dataframes
df = pd.read_sql(sql_sensorData, conn)
print(df.head())


# 1. Analyze data
print(df.dtypes)
print(df.info())
sns.heatmap(df.corr(),cmap='gnuplot')
plt.show()
df['HeartRate'].plot.hist()
plt.show()

# 2. Data Wrangling, remove all the unnecessary data/columns
# set different dataframes and columns together/concat to one final dataframe
# final_df = pd.concat([df,stress],axis=1)
final_df = df.drop(['HeartRateId','SessionId'],axis=1,inplace=True)

X = final_df.drop('Stress',axis=1)
y= final_df['Stress']
X = preprocessing.scale(X)


# 3. Training the model
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
model = LogisticRegression()
model.fit(X_train,y_train)

# 4. Testing the model: predict and accuracy
stress_predict = model.predict(X_test)
accuracy = model.score(X_test,y_test)
print('The accuracy of the model is :',accuracy)

