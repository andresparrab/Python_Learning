import sqlite3
import time
import datetime
import random
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

graph_data()
cursor.close()
conn.close()

