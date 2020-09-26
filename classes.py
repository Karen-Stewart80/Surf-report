import requests
import json


class Surf:
    
    def __init__(self):
        self.url='https://api.stormglass.io/v2/weather/point'
        self.waveHeight='waveHeight'
        self.windSpeed='windSpeed'
        self.data=self.get()
        self.chosen_time=self.times()
        self.wavereport=self.waves()
        self.windreport=self.wind()
      
        
    def get(self):
        
        params = {
            'lat':'28.0167',
            'lng': '153.4000',
            'params': 'waveHeight,windSpeed',
        }
        
        headers={
            'Authorization': '830cd6de-fc63-11ea-aa62-0242ac130002-830cd828-fc63-11ea-aa62-0242ac130002'
         }

        response=requests.get('https://api.stormglass.io/v2/weather/point',params=params,headers=headers)
       
        if response.status_code >= 400:
            print("Sorry, looks like an api error, try again.")
        return response
       
    def times(self):
        chosen_time= int(input("What time is your bodacious self looking to carve? \n "))
            
        return chosen_time
        
    
    def waves(self):
       # return waveHeight
       data= json.loads(self.data.text)
       return data['hours'][self.chosen_time]['waveHeight']['icon']
       
   
    def wind(self):
       #returns the windspeed
       data= json.loads(self.data.text)
       return data['hours'][self.chosen_time]['windSpeed']['icon']
   
    def surf_report(self):
      
        if self.wavereport < 2 :
            print("Dude, might need the Malibu. Perfect for all you new tube chasers")
    
     
        elif self.wavereport > 2 and self.wavereport< 4:
            print("Surf's up. Enjoy bros")
    
        elif self.wavereport > 4 and self.wavereport < 6 :
            print("Yewww. Barrels are pumping")
    
        else:
            print("Hectic! All you Bodhi's  gonna carve it up. Most excellent!")
     
        return f"Wave height is {self.wavereport} windspeed is {self.windreport}"

       
       
      
       
       
   