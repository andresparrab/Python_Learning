import  dash
from dash.dependencies import Output, Input
import  dash_html_components as html
import  dash_core_components as dcc
import plotly.graph_objs as go
import pyodbc  #this import microsoft sql database
import pandas as pd

# Parameters
server = 'localhost,1420'
db= 'CMRADatabase'

# Create the connection
#conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.4.so.2.1};SERVER=localhost,1420;DATABASE=CMRADatabase;UID=sa;PWD=Cmra1234')
conn = pyodbc.connect('DRIVER={SQL server};SERVER=localhost,1420;DATABASE=CMRADatabase;UID=sa;PWD=Cmra1234')


# Query
sql =""" 
    SELECT top (10) * FROM sensordata.HeartRate order by TimeStamp desc
"""


app = dash.Dash(__name__)

app.layout= html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=3000
        ),
    ]
)

@app.callback(Output('live-graph','figure'),
              [Input('graph-update','n_intervals')])
def update_awsome_graph(input_data):
    df = pd.read_sql(sql, conn)

    data = go.Scatter(
        x = df.Timestamp,
        y = df.HeartRate,
        name ='Scatter',
        mode ='lines+markers',

    )

    return {'data':[data], 'layout': go.Layout(xaxis=dict(range=[min(df.Timestamp), max(df.Timestamp)]),
                                               yaxis=dict(range=[min(df.HeartRate), max(df.HeartRate)]),)}



if __name__ == '__main__':
    app.run_server(debug=False)
