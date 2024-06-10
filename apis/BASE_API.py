import requests
import json

class BASE_API:
    def __init__(self):
        self.base_url = "http://hapi.fhir.org/baseR4/Observation/2529509/_history/1?_pretty=true"
        self.headers =  {
    "Accept-Charset": "utf-8",
    "Accept": "application/fhir+xml;q=1.0, application/fhir+json;q=1.0, application/xml+fhir;q=0.9, application/json+fhir;q=0.9",
    "User-Agent": "HAPI-FHIR/7.3.1-SNAPSHOT (FHIR Client; FHIR 4.0.1/R4; apache)",
    "Accept-Encoding": "gzip"
    }


    def get(self,endpoint,params = None):
        response = requests.get(url = self.base_url,headers= self.headers)
        return response