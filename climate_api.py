import requests

def get_dados(cidade):

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":cidade}

    headers = {
        "x-rapidapi-key": "63ea5ecf8bmsh5ea6c4f441a4064p13bff2jsn086fd722fb9f",
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

print(get_dados("Santa Luzia"))

