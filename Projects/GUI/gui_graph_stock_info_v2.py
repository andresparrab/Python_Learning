import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import datetime

# /////////////////////////////////////////////////////////////////////
# start = datetime.datetime(2015,2,20)
# end = datetime.datetime.now()
# stock = 'TSLA'
#
# df = web.DataReader(stock , 'stooq',start, end)

## //////////////////////////////////////////////////////////////////7
app = dash.Dash()


app.layout = html.Div(children=[
    html.Div( children=html.H1('''Symbol to graph: ''')),
    # create a dcc input field from dash core components
    dcc.Input(id='input',value='', type='text'), # this is where you will enter the text the field
    # Create a html component
    html.Div(id='output_graph')
    ])

# /////////////////////////////////////////////////////////////////////////
@app.callback(
    Output(component_id='output_graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
    )
def update_graph(input_data):
    start = datetime.datetime(2015, 2, 20)
    end = datetime.datetime.now()
    # stock = 'TSLA'

    df = web.DataReader(input_data, 'stooq', start, end)

    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x':df.index, 'y': df.Close, 'type':'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
         }
    )

if __name__ == '__main__':
    app.run_server(debug=False)





