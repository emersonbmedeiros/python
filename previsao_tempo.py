# Previsao do Tempo

import requests, json 

api_key = "3105bc8695e063633b9243c87efa0c09"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Qual Sua Cidade : ") 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
response = requests.get(complete_url) 
  
x = response.json() 
  
if x["cod"] != "404": 
  
    y = x["main"] 
  
    current_temperature = y["temp"] 
    
    current_pressure = y["pressure"] 
   
    current_humidiy = y["humidity"] 
   
    z = x["weather"] 
  
    weather_description = z[0]["description"] 
  
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 
else: 

    print(" Cidade Nao Encontrada ")
