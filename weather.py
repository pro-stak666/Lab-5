import requests
import geocoder
from pyowm import OWM

API_KEY = 'e3550dcaba1c67ca232279a38cbed61a'
HOST = 'https://api.openweathermap.org/data/2.5/'


def today(la='0', lo='0'):
    if la == '0' and lo == '0':
        g = geocoder.ip("me")
        lat = g.lat
        lon = g.lng
    else:
        lat = float(la)
        lon = float(lo)

    req = requests.get(f'{HOST}weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ru').json()
    res = {
        "city"      : req['name'],
        "dis"       : req['weather'][0]['description'],
        "temp"      : str(round(req['main']['temp'])) + "°C",
        "feels"     : str(round(req['main']['feels_like'])) + "°C",
        "pressure"  : str(round(req['main']['pressure'] / 1000 * 750, 2)) + " мм/р.с.",
        "wind"      : str(req['wind']['speed']) + ' м/с',
        "coords"    : f"{lat} {lon}"
    }
    return res


city = input("Введите город: ")
owm = OWM('e3550dcaba1c67ca232279a38cbed61a').weather_manager().weather_at_place(
                    city).to_dict()['location']['coordinates']
res = today(la=owm['lat'], lo=owm['lon'])
print(f"В городе {res['city']} сейчас {res['dis']}, температура водуха {res['temp']}, но ощущается как {res['feels']}")