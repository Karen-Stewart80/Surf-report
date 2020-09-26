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


# Do something with response data.
#data= json.loads(response.text)
#print(data['hours'][7]['waveHeight']['icon'])



class Surf:
    
    def __init__(self):
        self.url='https://api.stormglass.io/v2/weather/point'
        self.location='location'
        self.waveHeight='waveHeight'
        self.windSpeed='windSpeed'
        self.data=self.get()
        self.chosen_time=self.times()
        self.wavereport=self.waves()
        self.windreport=self.wind()
      
        
    def get(self):
       return requests.get('https://api.stormglass.io/v2/weather/point',params=params,headers=headers)
       
    def times(self):
        chosen_time= int(input("What time is your bodacious self looking to carve? \n "))
        return chosen_time
        
        
    def locations(self):
        #input location
        return "Surf Report for the Gold Coast"
    
    def waves(self):
       # return waveHeight
       data= json.loads(self.data.text)
       return data['hours'][self.chosen_time]['waveHeight']['icon']
       
   
    def wind(self):
       #returns the windspeed
       data= json.loads(self.data.text)
       return data['hours'][self.chosen_time]['windSpeed']['icon']
   
    def surf_report(self):
       return f"Wave height is {self.wavereport}windspeed is {self.windreport}"
       
word=Surf()

print(word.surf_report())
       
       
      
       
       
   