import requests

def fetch_weather(city, api_key):
  url=f"http://api.openweathermap.org/data/2.5/weather"
  params={"q":city,"appid":api_key,"units":"metric","lang":"kr"}
  response=requests.get(url,params=params)


  return response.json()

