import quandl, datetime
import  pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas_datareader.data as web
import datetime
quandl.ApiConfig.api_key = "gwFVwtxy45S5ixw9LPtU"

df = quandl.get("WIKI/GOOGL")

heart_rate = pd.DataFrame()


#heart_rate = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
heart_rate = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

data_dict = {"Heart Rate":heart_rate,
"Pupil Dialation": 'eye_pupils',
"Eye Openess": 'eye_open',
"Head_Height":'head_data',
"Head Angle":'head_data'
}

#print(heart_rate.groupby('Adj. Volume').size())
#print(heart_rate.tail())
#print(heart_rate.dtypes)
#print(heart_rate['Adj. Close'].index)

x= np.array(heart_rate.index)
y= np.array(heart_rate['Adj. Close'])
for x.any(item1) and y.any(item2):
    print(item1,item2)


#print(x)
# app = dash.Dash()
#
#
# app.layout = html.Div(children=[
#     html.H1('OMG!!! FINACE'),
#     #Make the Graph
#     dcc.Graph(id='example',
#               figure={
#                   'data': [
#                       {'x':heart_rate.index, 'y': y, 'type':'line', 'name': 'stock'},
#                     ],
#                   'layout': {
#                       'title': 'stock'
#                       }
#               })
#     ])
#
# if __name__== '__main__':
#     app.run_server(debug=True)