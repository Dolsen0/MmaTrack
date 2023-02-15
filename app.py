import http.client
from apiKey import apiKey

conn = http.client.HTTPSConnection("api.sportradar.us")

#conn.request("GET", "/mma/trial/v2/en/champions.json?api_key=" + apiKey)

#conn.request("GET", "/mma/trial/v2/en/schedules/2023-02-11/summaries.json?api_key=" + apiKey)

#conn.request("GET", "/mma/trial/v2/en/competitions.json?api_key=" + apiKey)

#pulls info on Aljo
#conn.request("GET", "/mma/trial/v2/en/competitors/sr:competitor:260623/profile.json?api_key=" + apiKey)

#pulls info on Valentina
conn.request("GET", "/mma/trial/v2/en/competitors/sr:competitor:246053/profile.json?api_key=" + apiKey)


res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
