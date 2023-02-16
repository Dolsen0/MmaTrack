import http.client
import json
from apiKey import apiKeys

conn = http.client.HTTPSConnection("api.sportradar.us")


conn.request("GET", "/mma/trial/v2/en/champions.json?api_key=" + apiKeys)

res = conn.getresponse()
data = res.read().decode("utf-8")

champions = json.loads(data)

def championSearch():
    for weight_class in champions['categories'][0]['weight_classes']:
        if weight_class['competitor']['name'] == 'Volkanovski, Alex':
            print(weight_class)

#create search instead of ==. volk could bring up volkanovski.,
#change to contains instead of ==