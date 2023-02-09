## 
# This program prints information about the current weather in a user-chosen city.
#

import urllib.request
import urllib.parse
import json

def main():
    latitude=int(input("Enter the latitude (nearest integer)"))
    longitude=int(input("Enter the longitude (nearest integer)"))
    getWeather(latitude, longitude)

    
def getWeather(lat, long):
    #add the # symbol to the latitude and longitude
    
    # Build and encode the URL parameters.
    params = {"lat": lat, "lon":long, "units": "imperial" }
    arguments = urllib.parse.urlencode(params)

    # Get the weather information.
    address = "http://api.openweathermap.org/data/2.5/weather"
    url = address + "?" + arguments
    print(url)
    webData = urllib.request.urlopen(url)
    results = webData.read().decode()
    webData.close()

    # Convert the json result to a dictionary.
    data = json.loads(results)
    #print (data)
    # Print the results.
    current = data["main"]
    degreeSym = chr(176)
    print("Temperature: %d%sF" % (current["temp"], degreeSym))
    print("Humidity: %d%%" % current["humidity"])
    print("Pressure: %d" % current["pressure"])
    #print(results)

#main()

