import sqlite3
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style


conn = sqlite3.connect('tutorial.db')
cursor = conn.cursor()

def graph_data():
    cursor.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    data = cursor.fetchall()
    for row in data:
        # print(row[0])
        # print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates,values, ':')
    plt.show()


def del_and_update():
    cursor.execute('SELECT * FROM stuffToPlot')
    data = cursor.fetchall()
    [print(row) for row in data]
    print(50*'//')
    # Set the value 99 everywhere where de value is2, OBS this is permanent
    cursor.execute('UPDATE stuffToPlot SET value = 99 WHERE value =2')
    # conn.commit() save the changes
    conn.commit()

    # Select the table again and showthen new values

    cursor.execute('SELECT * FROM stuffToPlot')
    data = cursor.fetchall()
    [print(row) for row in data]

    # this will delete the first 3  rows where the value is 99, witout LIMIT it will delete all rows value=99
    cursor.execute('DELETE FROM stuffToPlot WHERE value = 99')
    conn.commit()
    print(50*'#')


    cursor.execute('SELECT * FROM stuffToPlot')
    data = cursor.fetchall()
    [print(row) for row in data]

    # fetch how many rows has value of 0,is good to know before delete or update
    cursor.execute('SELECT * FROM stuffToPlot WHERE value = 0')
    data = cursor.fetchall()
    print(50*'...')
    [print(row) for row in data]
    print(len(data))

del_and_update()
cursor.close()
conn.close()

