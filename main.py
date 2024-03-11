from weather_check import get_weather

# import time for function to convert epoch to normal time for sunset and sunrise
import time; 

import os
# function to clear screen.
def clear():
    # posix is os name for Linux or mac
    if(os.name == 'posix'):
        os.system('clear')
    # else screen will be cleared for window
    else:
        os.system('cls')
        # Channge Color for window
        os.system('color F0')   
    
    
while True:
    clear()
    print(""" ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
 ║                                            🌞  WELCOME TO YOUR OWN PERSONAL WEATHER ASSISTANT! ⛅                                               ║
 ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝""")
    print(""" ╔═════════════════════════════════════════╗                                                              
 ║ 🌆  Pick the city to check its weather. ║ 
 ╚═════════════════════════════════════════╝ """)

    # loop for city input error handling
    while True:
        city = input(" >> Enter here 👉 : ")
        weather_data = get_weather(city)
        
        if weather_data['cod'] == '404':
            print(""" ╔════════════════════════════════════════════╗                                                              
 ║ ❗❗ Invalid City ❗❗ Please try again 👇 ║ 
 ╚════════════════════════════════════════════╝ """)
            continue
        else:
            break
    # end of city input error handling loop
    
    weather = weather_data["weather"][0]
    main = weather_data["main"]
    wind = weather_data["wind"]
    visibility = weather_data["visibility"]
    
    # formulas to convert epoch time to normal time
    sunrise = time.strftime("%H:%M:%S", time.localtime(weather_data["sys"]["sunrise"])) 
    sunset = time.strftime("%H:%M:%S", time.localtime(weather_data["sys"]["sunset"])) 
    
    print(f"\n 🌞  Weather Overview of {city.capitalize()} ⛅")
    print(f""" ╔════════════════════════════════════╗   
     ☁️  Weather     : {weather["description"].capitalize()}
     🌡️  Tempurature : {main["temp"]} °C  
     🌫️  Feels like  : {main["feels_like"]} °C     
     ⏲️  Pressure    : {main["pressure"]} hPa
     💦 Humidity    : {main["humidity"]} %
     🌪️  Wind Speed  : {wind["speed"]} km/h
     👁️  Visibility  : {visibility} km
     🌄 Sunrise     : {sunrise}
     🌅 Sunset      : {sunset}
 
 ╚════════════════════════════════════╝""")
    
    print("""
 ╔═════════════════════════════════╗                                                              
 ║    Do you want to try again?    ║ 
 ║    1. Try Again                 ║ 
 ║    2. Exit                      ║ 
 ╚═════════════════════════════════╝ """)
    # while for try again
    while True:
        action = input(">> Enter here: ").lower()
        if action == "1" or action == "try again":
            break
        elif action == "2" or action == "exit":
            print(""" ╔═════════════════════════════════╗                                                              
 ║          Goodbye, User!         ║ 
 ╚═════════════════════════════════╝ """)
            exit()
        else:
            print(""" ╔═════════════════════════════════════╗                                                              
 ║       ❗❗ Invalid Choice ❗❗      ║ 
 ╚═════════════════════════════════════╝ """)