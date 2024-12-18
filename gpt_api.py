import requests
from config import CHAVE_GPT
from climate_api import get_dados

def ler_prompt(nome):
    caminho_arquivo = "prompt_gpt.txt"

    with open (caminho_arquivo, "r", encoding='utf-8') as arquivo:
        prompt = arquivo.read() + f"\n\nO nome do usuário é {nome}"

    return prompt

def get_gpt(cidade, nome):
    informacoes = get_dados(cidade)

    prompt = ler_prompt(nome)

    url = "https://api.openai.com/v1/chat/completions"

        # Cabeçalhos da requisição
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHAVE_GPT}"
    }

    # Corpo da requisição (dados que você vai passar)
    data = {
        "model": "gpt-3.5-turbo",  # ou outro modelo, como gpt-4
        "messages": [{"role": "system", "content": informacoes},
        {"role": "user", "content": prompt}]
    }

    # Fazer a requisição POST
    response = requests.post(url, headers=headers, json=data)

    result = response.json()
    return result["choices"][0]["message"]["content"]