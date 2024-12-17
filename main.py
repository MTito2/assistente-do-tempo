from gpt_api import get_gpt
from enviar_email_api import enviar_email
from datetime import datetime
from verificar_email import verifica_email

hoje = datetime.now().strftime('%d-%m-%Y')
assunto = f"Relatorio do tempo {hoje}"

while True:
    print("Bem vindo ao Assistente do tempo")
    cidade = input("Informe a cidade: ")
    nome = input("Informe seu nome: ")

    print("Gerando relatório...")

    op = input("Deseja receber o relatório por email? [S/N] ")

    if op.upper() in ("SIM", "S"):

        email = input("Informe o email: ")
        verificacao_email = verifica_email(email)

        while verificacao_email is False:
            print("Email inválido")
            email = input("Informe o email: ")
            verificacao_email = verifica_email(email)

        corpo_email = get_gpt(cidade, nome) 
        enviar_email(email, assunto, corpo_email)

    else:
        resposta = get_gpt(cidade, nome)
    
    sair = input("Deseja encerrar o programa? [S/N] ")
    if sair.upper() in ("SIM", "S"):
        break 
    
    else:
        continue
    