import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()


app.layout = html.Div(children=[
    # create a dcc input field from dash core components
    dcc.Input(id='input',value='', type='text'), # this is where you will enter the text the field
    # Create a html component
    html.Div(id='output')
    ])

# we are goin to do a function that handles the input and give/produce us an output
#the next line is a wrapper decorator
@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')])
def update_value(input_data): # This will update the data you write in real time from the input field
    try:
        return 'The power is: ',str(float(input_data)**2)
    except:
        return 'Please enter a number!!'


if __name__== '__main__':
    app.run_server(debug=True)