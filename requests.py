import requests
def findall():
    api_url = "http://192.168.0.105:8090/countries"
    response = requests.get(api_url)
    print (response.json())
def create():
    api_url = f"http://192.168.0.105:8090/countries"
    lista = {"id": 4, "name": "China", "capital": "Hong kong", "area": 51}
    response = requests.post(api_url,json= lista)
    print (response.json())
def findbyid(id):
    api_url = f"http://192.168.0.105:8090/countries/{id}"
    response = requests.get(api_url)
    print (response.json())
def update(id):
    insert = {"id": 5, "name": "e", "capital": "BevellyHills", "area": 51}
    api_url = f"http://192.168.0.105:8090/countries/{id}"
    response = requests.put(api_url, json= insert)
    print (response.json())
def delete(id):
    api_url = f"http://192.168.0.105:8090/countries/{id}"
    response = requests.delete(api_url)
    print (response.json())
