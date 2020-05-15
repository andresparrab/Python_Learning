import numpy as np
import  dash
import  dash_html_components as html
import  dash_core_components as dcc

x= np.array(range(0,21))
y= np.array(range(10,31))

x1 = []
y1= []
for item in x:
    for item2 in y:
        if 18<item2<22:
            if 8<item<12:
                print('Personen i frågran är stressad  ',item,item2)
                x1.append(item)
                y1.append(item2)


print('X one is: ',x1)
print('Y one is :  ',y1)


app = dash.Dash()
app.layout = html.Div(children=[
    html.H1('Stress'),


    #Make the Graph
    dcc.Graph(id='example',
              figure={
                  'data': [
                      {'x':x, 'y':y, 'type':'line', 'name': 'Heart rate'},
                      {'x':x1, 'y':y1, 'mode': 'markers', 'name': 'Stress1'}
                    ],

                  'layout': {
                      'title': 'Graphs'
                      }
              })
    ])

if __name__== '__main__':
    app.run_server(debug=False)