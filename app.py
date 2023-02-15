import http.client
from apiKey import apiKey

conn = http.client.HTTPSConnection("api.sportradar.us")

#conn.request("GET", "/mma/trial/v2/en/champions.json?api_key=" + apiKey)
#conn.request("GET", "/mma/trial/v2/en/schedules/2023-02-11/summaries.json?api_key=" + apiKey)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
