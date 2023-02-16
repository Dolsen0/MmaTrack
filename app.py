import http.client
import json
from apiKey import apiKeys
from championSearch import championSearch

conn = http.client.HTTPSConnection("api.sportradar.us")

#champions list

#conn.request("GET", "/mma/trial/v2/en/schedules/2023-02-11/summaries.json?api_key=" + apiKey)

#conn.request("GET", "/mma/trial/v2/en/competitions.json?api_key=" + apiKey)

#pulls info on Aljo
#conn.request("GET", "/mma/trial/v2/en/competitors/sr:competitor:260623/profile.json?api_key=" + apiKey)

#pulls info on Valentina
#conn.request("GET", "/mma/trial/v2/en/competitors/sr:competitor:246053/profile.json?api_key=" + apiKey)

championSearch()