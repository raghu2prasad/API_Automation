import requests
import json

url = "http://hapi.fhir.org/baseR4/Observation/2529509/_history/1?_pretty=true"
headers = {"Server": "Jetty(12.0.8)",
 "X-Powered-By":"HAPI FHIR 7.3.1-SNAPSHOT/d413af1777/2024-05-11 REST Server (FHIR Server; FHIR 4.0.1/R4)",
           "Content-Type": "application/fhir+xml;charset=utf-8"}
response = requests.get(url = url)
print(response.status_code)
assert response.status_code == 200
print(response.json())