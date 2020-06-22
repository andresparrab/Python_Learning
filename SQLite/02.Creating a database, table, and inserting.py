import sqlite3
import time
import datetime
import random


conn = sqlite3.connect('tutorial.db')
cursor = conn.cursor()

def create_table():
    # Create a SQL table with name stuffToPlot and the columns name, unix,datestamp,keyword and value.
    # notice Real type means real number, a float. and text is normal text
    # The capilasied words are sql code
    cursor.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix Real, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    cursor.execute("INSERT INTO stuffToPlot VALUES(1453454,'2016-01-01', 'Python', 8)")
    # every time you want to modified something, it has to follow by the code below to save
    conn.commit()
    cursor.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    cursor.execute('INSERT INTO stuffToPlot (unix,datestamp,keyword,value) VALUES (?,?,?,?)',
                   (unix,date,keyword,value))
    conn.commit()


create_table()
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
cursor.close()
conn.close()




# create the table and input the values
# OBS if you run this multiples time it will add more rows with same values or if you change the data_entry
# it will add new row with the different values
# create_table()
# data_entry()