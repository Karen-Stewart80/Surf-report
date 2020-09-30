##Surf Report Application

#####R1	1) Develop and describe an algorithmic solution for an application that utilises two way communication over a network (300 - 500 words)

Surf Report application will utilise two way communication over a network. StormGlass api is an api that offers a wide range of marine and weather data, everything from air temperature to wave height. Because of the wide range of data available, the Surf Report will limit its reporting to wave height and windspeed.  Surf Report is an application that welcomes the user and then asks them to input a time that they would like to go surfing. The welcome and questioning is written in stereotypical surfer lingo. The time is converted to an integer by the app. The app then communicates with Storm Glass api utilising the the integer that was input by the user to access the data for the appropriate time. The user input is not actually the time, but rather the index for an array for the time in Storm Glass api. For example 7 in the morning would access index 7 of the api in the hours array. The app asks for the data of wave height and wind speed and Storm Glass api returns that information to the app. The app then tells the user in surfer lingo how good the waves are and adds the numerical value for the wave height and windspeed. If the user input is not an acceptable number, the app will tell the user to try again. The app is structured with main.py python file, classes.py python file and a test.py python file. The main.py file contains the current time, welcome and calls the class Surf to run and print. The app uses functions inside the class Surf to find the correct wave height and windspeed for the entered time. Surf Report app utilises the longitude and latitude for the Gold Coast and does not offer change of location as this is an application for Gold Coast locals.

###Installation

Create your python virtual environment and in bash run

```python
pip install -r requirements.txt

export API_KEY=830cd6de-fc63-11ea-aa62-0242ac130002-830cd828-fc63-11ea-aa62-0242ac130002

cd Surf-report

python3.8 main.py
```

###Instructions for Surf-report application

How to use Surf-report App.
    The app will greet you and ask what time you would like surf.
    Enter a single or double digit number. For example for 7am enter 7
    The app will then tell you the wave height and windspeed for that time on the Gold Coast
    Depending on the wave height, the app will respond with a chosen message in surfer lingo.
    