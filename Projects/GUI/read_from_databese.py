import pandas as pd
import pyodbc  #this import microsoft sql database

# Parameters
server = 'localhost,1421'
db= 'Customer'

# Create the connection
conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.4.so.2.1};SERVER=localhost,1421;DATABASE=Customer;UID=sa;PWD=Cmra1234')

# Query
sql =""" 
    SELECT * FROM dbo.Heartrate
"""

df= pd.read_sql(sql,conn)
print(df.head(50))