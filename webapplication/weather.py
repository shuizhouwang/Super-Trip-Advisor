import pandas as pd
import requests
import json
def return_weather(geo):
    latstr=str(geo['lat'])
    lngstr=str(geo['long'])
    key = "3977c6033ed34b1909d97411b8215e52"
    mid = "&appid="
    url = "http://api.openweathermap.org/data/2.5/weather?"
    info = 'lat=' + latstr + '&lon=' + lngstr
    url = url + info + mid + key 
    r = requests.get(url)
    info=r.json()
    weather = info["weather"][0]["description"]
    return weather
  