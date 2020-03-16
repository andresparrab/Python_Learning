import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pyodbc  #this import microsoft sql database
import pandas as pd
from plotly.subplots import make_subplots

# Parameters
server = 'localhost,1420'
#server = 'cmra_db,1433'
db= 'CMRADatabase'
password = 'Cmra1234'
data_length = '20'

# Create the connection for runnning outside the container
conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.4.so.2.1};SERVER=' + server +';DATABASE=' +db + ';UID=sa;PWD=' + password)
# Create the connection for running inside the container
#conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.5.so.1.1};SERVER=' + server +';DATABASE=' +db + ';UID=sa;PWD=' + password)
#Create the connection for running in windods
#conn = pyodbc.connect('DRIVER={SQL server};SERVER=localhost,1420;DATABASE=CMRADatabase;UID=sa;PWD=Cmra1234')

# Query
sql_hear_rate ='SELECT top (' + data_length + ') * FROM sensordata.HeartRate order by TimeStamp desc'

sql_eye_data='SELECT top (' + data_length + ') * FROM sensordata.EyeData order by TimeStamp desc'

sql_head_data='SELECT top (' + data_length + ') * FROM sensordata.Head order by TimeStamp desc'

heart_rate= pd.DataFrame()
eye_pupils= pd.DataFrame()
eye_open= pd.DataFrame()
head_data= pd.DataFrame()


#import the css and java scripts from Materialize
external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']

# define the app, and then we'll specify a dictionary for the datapoints we intend to cover:
app = dash.Dash('Monitor',
                external_scripts=external_js,
                external_stylesheets=external_css)

# This is for the dropdown menu in dictionary form  when you choose for example Speed
# it will get the speeds for the graph
data_dict = {"Heart Rate":heart_rate,
"Pupil Dialation": eye_pupils,
"Eye Openess": eye_open,
"Head":head_data
}

#def get_data (heart_rate, eye_pupils, eye_open, head_data):
def get_data ():

    df_hr = pd.read_sql(sql_hear_rate, conn)
    heart_rate = df_hr.Timestamp,df_hr.HeartRate

    df_eye_pupils = pd.read_sql(sql_eye_data, conn)
    eye_pupils = df_eye_pupils.Timestamp,df_eye_pupils.PupilDiameterMM_L,df_eye_pupils.PupilDiameterMM_R

    df_eye_open = pd.read_sql(sql_eye_data, conn)
    eye_open = df_eye_open.Timestamp,df_eye_open.Openness_L,df_eye_open.Openness_R

    df_head_data= pd.read_sql(sql_head_data, conn)
    head_data = df_head_data.Timestamp,df_head_data.Height_from_floor,df_head_data.Pitch,df_head_data.Roll


    data_dict = {"Heart Rate":heart_rate,
    "Pupil Dialation": eye_pupils,
    "Eye Openess": eye_open,
    "Head":head_data
}

    #return heart_rate, eye_pupils, eye_open, head_data
    return data_dict


# structure of this app, the layout:

app.layout = html.Div([
    html.Div([
        html.H2('Sensors Monitor',
                style={'float': 'left',
                       }),
        ]),
    dcc.Dropdown(id='data-name',
                 options=[{'label': s, 'value': s}
                          for s in data_dict.keys()],
                 value=['Heart Rate','Pupil Dialation','Head'],
                 multi=True
                 ),

    html.Div(children=html.Div(id='graphs'), className='row'),

    dcc.Interval(
        id='graph-update',
        interval=1000),
    ], className="container",style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000})

#   write the decorator first. This one is interesting, since, actually, we're going to have Input, Output, AND events!
@app.callback(
    dash.dependencies.Output('graphs','children'),
    [dash.dependencies.Input('data-name', 'value'),
# events=[dash.dependencies.Event('graph-update', 'interval')], THIS IS NOT LONGER SUPPORTED IN DASH
# use the line below, tha will act as an event, and basicaly update the graphs
    dash.dependencies.Input('graph-update', 'n_intervals')]
    )
# The function that updates the graphs
def update_graph(data_names, n):

    # this is what we will return, a list of graphs
    graphs = []
    data_dict = get_data()
    #print(data_dict)

    if len(data_names)>2:
        class_choice = 'col s12 m6 l4'
    elif len(data_names) == 2:
        class_choice = 'col s12 m6 l6'
    else:
        class_choice = 'col s12'

    for data_name in data_names:
        #print(data_dict[data_name])

        if data_name == "Head":
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            fig.add_trace(
                #data=go.Scatter(
                go.Scatter(

                    x=data_dict[data_name][0],
                    y=data_dict[data_name][1],
                    name='Scatter1',
                    mode='lines',
                    fillcolor="#6897bb",

            ),secondary_y = False,
            )
            fig.add_trace(
                #data=go.Scatter(
                go.Scatter(

                    x=data_dict[data_name][0],
                    y=data_dict[data_name][2],
                    name='Scatter',
                    mode='markers',
                    fillcolor="#bb7668",

                ),secondary_y = True,
            )




            graphs.append(html.Div(dcc.Graph(
                id=data_name,
                animate=True,
                #figure={'data': [data], 'layout': go.Layout(
                figure={'data': [fig], 'layout': go.Layout(
                    xaxis=dict(range=[min(data_dict[data_name][0]), max(data_dict[data_name][0])]),
                    yaxis=dict(range=[min(data_dict[data_name][1]), max(data_dict[data_name][1])]),
                    margin={'l': 50, 'r': 1, 't': 45, 'b': 1},
                    title='{}'.format(data_name))}
            ), className=class_choice))

        else:

            data = go.Scatter(

                x=data_dict[data_name][0],
                y=data_dict[data_name][1],

                name='Scatter',
                fill="tozeroy",
                fillcolor="#6897bb"
                )

            graphs.append(html.Div(dcc.Graph(
                id=data_name,
                animate=True,
                figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(data_dict[data_name][0]),max(data_dict[data_name][0])]),
                                                            yaxis=dict(range=[min(data_dict[data_name][1]),max(data_dict[data_name][1])]),
                                                            margin={'l':50,'r':1,'t':45,'b':1},
                                                            title='{}'.format(data_name))}
            ), className=class_choice))
    return graphs

if __name__== '__main__':
    app.run_server(host='0.0.0.0',debug=False)