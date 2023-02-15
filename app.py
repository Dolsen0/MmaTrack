import http.client
from apiKey import apiKey

conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", "/mma/trial/v2/en/champions.xml?api_key=" + apiKey)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
