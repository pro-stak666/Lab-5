from requests import get
from datetime import datetime
from time import sleep
import os

res = get('http://api.open-notify.org/iss-now.json').json()
date = datetime.utcfromtimestamp(res['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
la = res['iss_position']['latitude']
lo = res['iss_position']['longitude']
while True:
    print('Положение Мкс')
    print(f'Время: {date}, Широта: {la}, Долгота: {lo}')
    res = get('http://api.open-notify.org/iss-now.json').json()
    date = datetime.utcfromtimestamp(res['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
    la = res['iss_position']['latitude']
    lo = res['iss_position']['longitude']
    sleep(3)
    os.system('cls')