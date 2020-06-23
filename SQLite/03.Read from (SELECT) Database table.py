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

def read_from_db():
    # This will selec everything from the database
    # cursor.execute('SELECT * FROM stuffToPlot')
    # This will Select every row that has the value=3 andthe word Python
    # cursor.execute("SELECT * FROM stuffToPlot WHERE value=3 AND keyword='Python'")
    # This will Select every row that has the unix time greater than 1592893523.5213718 and order
    # by keyword column first then unx then value
    cursor.execute("SELECT keyword, unix, value FROM stuffToPlot WHERE unix >1592893523.5213718 ")
    # this will save all the data into the variable data
    data = cursor.fetchall()
    # print(data)
    for row in data:
        print(row)




read_from_db()
# create_table()
# for i in range(10):
#     dynamic_data_entry()
#     #we put time.sleep(1) so the timestamp updates 1 second in the table
#     time.sleep(1)
cursor.close()
conn.close()

