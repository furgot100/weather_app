from flask import Flask, render_template, request
import requests
import pprint

app = Flask(__name__)


pp = pprint.PrettyPrinter(indent=4)
weather_url = 'http://api.openweathermap.org/data/2.5/weather'

app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    return render_template('weather_form.html')

@app.route('/weather_results')
def weather_results():
    user_city = request.args.get('city')
    API_KEY = '8f23d9ba5e589062e1110c726b2bdb57'
    
    params = {
        'q' : user_city,
        'appid': API_KEY
    }
    
    r = requests.get(weather_url, params=params)

    if not r.status_code == 200:
        print("error")
    results = r.json()
    city = results['name']
    temp = convertions(results['main']['temp'])
    return render_template('results.html', city=city, temp=temp)

    # print("It is now " + str(temp_in_kelvin) + " degrees in kelvin.")

    # return render_template('results.html', weather=weather)


def convertions(temp):
    result = 1.8 * (temp-273) +32
    return int(result)


# # print("It is now " + str(temp_in_kelvin) + " degrees in kelvin.")



if __name__ == '__main__':
    app.run()