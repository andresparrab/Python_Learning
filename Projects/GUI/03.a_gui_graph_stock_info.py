import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas_datareader.data as web
import datetime

start = datetime.datetime(2016,2,20)
end = datetime.datetime.now()

stock = 'TSLA'

df = web.DataReader(stock , 'stooq',start, end)
print(df.head())



app = dash.Dash()


app.layout = html.Div(children=[
    html.H1('OMG!!! FINACE'),
    #Make the Graph
    dcc.Graph(id='example',
              figure={
                  'data': [
                      {'x':df.index, 'y': df.Close, 'type':'line', 'name': stock},
                    ],
                  'layout': {
                      'title': stock
                      }
              })
    ])

if __name__== '__main__':
    app.run_server(debug=True)