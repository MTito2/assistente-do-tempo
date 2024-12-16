import requests
from config import CHAVE_GPT
from climate_api import get_dados

def ler_prompt():
    caminho_arquivo = "prompt_gpt.txt"

    with open (caminho_arquivo, "r", encoding='utf-8') as arquivo:
        prompt = arquivo.read()
        
    return prompt

def get_gpt(informacoes):
    prompt = ler_prompt()

    url = "https://chatgpt-42.p.rapidapi.com/gpt4"

    payload = {
        "messages": [
            {
                "role": "user",
                "content": {"prompt":prompt, "info": informacoes}}
        ],
        "web_access": False
    }
    headers = {
        "x-rapidapi-key": CHAVE_GPT,
        "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()

