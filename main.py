from gpt_api import get_gpt
from enviar_email_api import enviar_email
from datetime import datetime
from verificar_email import verifica_email
import os

hoje = datetime.now().strftime('%d-%m-%Y')
assunto_email = f"Relatorio do tempo {hoje}"

while True:
    print("Bem vindo ao Assistente do tempo")
    cidade = input("Informe a cidade: ")
    nome = input("Informe seu nome: ")
    os.system("cls")

    print("Gerando relatório...")
    print(60 * "=")

    op = input("Deseja receber o relatório por email? [S/N] ")
    os.system("cls")

    if op.upper() in ("SIM", "S"):

        email = input("Informe o email: ")
        verificacao_email = verifica_email(email)
        os.system("cls")


        while verificacao_email is False:
            os.system("cls")
            print("O email parece ser inválido")

            email = input("Informe o email: ")
            verificacao_email = verifica_email(email)
            os.system("cls")


        corpo_email = get_gpt(cidade, nome) 
        enviar_email(email, assunto_email, corpo_email)

    else:
        resposta = get_gpt(cidade, nome)
        print()
        print(resposta)
    
    sair = input("Deseja encerrar o programa? [S/N] ")
    if sair.upper() in ("SIM", "S"):
        break 
    
    else:
        os.system("cls")
        continue
    