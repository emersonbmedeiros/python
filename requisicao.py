import requests
import json

cidade = input("Qual sua cidade: ")
requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=3105bc8695e063633b9243c87efa0c09')

tempo = json.loads(requisicao.text)
print(tempo)
print('Condicao do tempo em ' +cidade+ ':', tempo['weather'][0] ['main'])
print('Temperatura', float(tempo['main']['temp']) - 273.15)
