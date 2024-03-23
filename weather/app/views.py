from django.shortcuts import render
import json
import urllib.request
from config import API_KEY
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        res = urllib.request.urlopen(url).read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "main": str(json_data['weather'][0]['main']),
            "description": str(json_data['weather'][0]['description']),
            "icon": json_data['weather'][0]['icon'],
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
        
    
