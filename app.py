from flask import Flask, render_template, request
import requests
import pprint

app = Flask(__name__)

app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    return render_template('weather_form,html')

@app.route('/weather_results')
def weather_results():
    user_city = request.args.get('city')
    API_KEY = '8f23d9ba5e589062e1110c726b2bdb57'
    
    weather = {
        'name' : user_city,
        'appid': API_KEY
    }
    
    return render_template('weather_results.html', weather=weather)


pp = pprint.PrettyPrinter(indent=4)

weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=San+Francisco&appid=8f23d9ba5e589062e1110c726b2bdb57'

response = requests.get(weather_url)
response_json= response.json()
# pp.pprint(response_json)

main_data = response_json["main"]
temp_in_kelvin = main_data["temp"]
pp.pprint(response_json)
# print("It is now " + str(temp_in_kelvin) + " degrees in kelvin.")