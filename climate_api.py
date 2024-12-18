import requests
from config import CHAVE_WEATHER

def get_dados(cidade):
    string = ""

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":cidade}

    headers = {
        "x-rapidapi-key": CHAVE_WEATHER,
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    response = response.json()
   

    for chave, valor in response.items():
        string += (f"{str(chave):}" + f"{str(valor)}")

    return string
    


