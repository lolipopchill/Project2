from flask import Flask, render_template, request
import requests
<<<<<<< HEAD
from dashboard import dash_app, server
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

app = Flask(__name__)

API_KEY = 'yXcUn6haV3nAcW1UlLUlbe6LEozZwVUu'
=======

app = Flask(__name__)

API_KEY = 'yXcUn6haV3nAcW1UlLUlbe6LEozZwVUu'   #лучше вставить свой ключ
>>>>>>> 9d6e9dbc4965aab0eb80fa6cc4c5316b73c32081

def get_weather_data(city, api_key):
    url = f"http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {'apikey': api_key, 'q': city}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        location_data = response.json()
        if location_data:
            location_key = location_data[0]['Key']
            forecast_url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}"
            forecast_params = {'apikey': api_key, 'metric': 'true', 'details': 'true'}
            forecast_response = requests.get(forecast_url, params=forecast_params)
            if forecast_response.status_code == 200:
                forecast_data = forecast_response.json()
                if 'DailyForecasts' in forecast_data and len(forecast_data['DailyForecasts']) > 0:
                    daily_forecast = forecast_data['DailyForecasts'][0]
                    temperature = daily_forecast['Temperature']['Maximum']['Value']
                    wind_speed_kmh = daily_forecast['Day'].get('Wind', {}).get('Speed', {}).get('Value', 0)
                    wind_speed_ms = round(wind_speed_kmh * 0.27778, 2)
                    precipitation_probability = daily_forecast['Day'].get('PrecipitationProbability', 0)
                    return {
                        'city': city,
                        'temperature': temperature,
                        'wind_speed': wind_speed_ms,
                        'precipitation_probability': precipitation_probability
                    }
    return None

def is_bad_weather(weather_data):
<<<<<<< HEAD
    """Определяем плохие погодные условия по температуре, ветру и осадкам."""
=======
>>>>>>> 9d6e9dbc4965aab0eb80fa6cc4c5316b73c32081
    if weather_data['temperature'] < -5 or weather_data['temperature'] > 35:
        return True
    if weather_data['wind_speed'] > 50:
        return True
    if weather_data['precipitation_probability'] > 70:
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_info_start = None
    weather_info_end = None
    error_message = None
    weather_condition_start = "Хорошая погода"
    weather_condition_end = "Хорошая погода"

    if request.method == 'POST':
        city_start = request.form.get('city_start')
        city_end = request.form.get('city_end')

        if city_start and city_end:
            weather_info_start = get_weather_data(city_start, API_KEY)
            weather_info_end = get_weather_data(city_end, API_KEY)

            if weather_info_start and weather_info_end:
<<<<<<< HEAD
                update_dashboard_data(weather_info_start, weather_info_end)
                
=======
>>>>>>> 9d6e9dbc4965aab0eb80fa6cc4c5316b73c32081
                if is_bad_weather(weather_info_start):
                    weather_condition_start = "Плохая погода"
                if is_bad_weather(weather_info_end):
                    weather_condition_end = "Плохая погода"
            else:
                error_message = 'Ошибка получения данных о погоде. Проверьте названия городов.'
        else:
            error_message = 'Пожалуйста, введите названия начальной и конечной точки маршрута.'

    return render_template('index.html', 
                           weather_info_start=weather_info_start,
                           weather_info_end=weather_info_end,
                           error_message=error_message,
                           weather_condition_start=weather_condition_start,
                           weather_condition_end=weather_condition_end)

<<<<<<< HEAD
def update_dashboard_data(weather_start, weather_end):
    @dash_app.callback(
        Output('weather-comparison', 'figure'),
        [Input('parameter-selector', 'value')]
    )
    def update_graph(selected_parameter):
        cities = [weather_start['city'], weather_end['city']]
        values = [weather_start[selected_parameter], weather_end[selected_parameter]]
        
        return {
            'data': [
                go.Bar(
                    x=cities,
                    y=values,
                    marker=dict(color=['#1f77b4', '#ff7f0e'])
                )
            ],
            'layout': go.Layout(
                title=f'Сравнение {selected_parameter}',
                xaxis={'title': 'Город'},
                yaxis={'title': get_parameter_label(selected_parameter)}
            )
        }

def get_parameter_label(parameter):
    labels = {
        'temperature': 'Температура (°C)',
        'wind_speed': 'Скорость ветра (м/с)',
        'precipitation_probability': 'Вероятность осадков (%)'
    }
    return labels.get(parameter, parameter)

=======
>>>>>>> 9d6e9dbc4965aab0eb80fa6cc4c5316b73c32081
if __name__ == '__main__':
    app.run(debug=True)
