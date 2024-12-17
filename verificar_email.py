import re

def verifica_email(email):

    expressao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
    if re.match(expressao, email):
        valido = True

    else:
        valido = False
    
    return valido




    