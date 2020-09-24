import requests
import json
from datetime import datetime
from time import time

#current=time.time

now=datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


import datetime


print(datetime.datetime.fromtimestamp(
        int("1284105682")
    ).strftime('%Y-%m-%d %H:%M:%S')
)

params = {
    
    'lat':'28.0167',
    'lng': '153.4000',
    'params': 'waveHeight,windSpeed',
}

headers={
    'Authorization': '830cd6de-fc63-11ea-aa62-0242ac130002-830cd828-fc63-11ea-aa62-0242ac130002'
 }


response = requests.get('https://api.stormglass.io/v2/weather/point',params=params,headers=headers)

print(response.text)
# Do something with response data.
json_data = response.json()


class Surf:
    
    def __init__(self):
        self.url='https://api.stormglass.io/v2'
        self.location='location'
        self.waveHeight='waveHeight'
        self.windSpeed='windSpeed'
        
    def locations(self):
        #input location
        pass
    
    def waves(self):
       # return waveHeight
       pass
   
    def wind(self):
       #returns the windspeed
       pass
   