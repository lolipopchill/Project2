from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from flask import Flask
import pandas as pd

server = Flask(__name__)
dash_app = Dash(__name__, server=server, url_base_pathname='/dashboard/')

dash_app.layout = html.Div([
    html.H1('Визуализация погодных данных'),
    
    html.Div([
        dcc.Dropdown(
            id='parameter-selector',
            options=[
                {'label': 'Температура', 'value': 'temperature'},
                {'label': 'Скорость ветра', 'value': 'wind_speed'},
                {'label': 'Вероятность осадков', 'value': 'precipitation_probability'}
            ],
            value='temperature'
        )
    ]),
    
    dcc.Graph(id='weather-comparison'),
])

@dash_app.callback(
    Output('weather-comparison', 'figure'),
    [Input('parameter-selector', 'value')]
)
def update_graph(selected_parameter):
    return {
        'data': [],
        'layout': go.Layout(
            title=f'Сравнение {selected_parameter}',
            xaxis={'title': 'Город'},
            yaxis={'title': selected_parameter.capitalize()}
        )
    } 