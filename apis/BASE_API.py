import requests
import json

url = "http://hapi.fhir.org/baseR4/Observation/2529509/_history/1?_pretty=true"
headers = {
    "Accept-Charset": "utf-8",
    "Accept":"application/fhir+xml;q=1.0, application/fhir+json;q=1.0, application/xml+fhir;q=0.9, application/json+fhir;q=0.9",
           "User-Agent": " HAPI-FHIR/7.3.1-SNAPSHOT (FHIR Client; FHIR 4.0.1/R4; apache)"}
#           "Accept-Encoding" : "gzip"}
headers1 = {
    "Accept-Charset": "utf-8",
    "Accept": "application/fhir+xml;q=1.0, application/fhir+json;q=1.0, application/xml+fhir;q=0.9, application/json+fhir;q=0.9",
    "User-Agent": "HAPI-FHIR/7.3.1-SNAPSHOT (FHIR Client; FHIR 4.0.1/R4; apache)",
    "Accept-Encoding": "gzip"
}

response = requests.get(url = url,headers=headers1)
print(response.status_code)
assert response.status_code == 200
#print(response.json())
print(response.text)
print(type(response.text))