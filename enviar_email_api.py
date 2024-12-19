import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from config import EMAIL_GMAIL, SENHA_APP_GMAIL

def enviar_email(destinatario, assunto, corpo):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email = EMAIL_GMAIL
    password = SENHA_APP_GMAIL

    # Criando o objeto do e-mail
    message = MIMEMultipart()
    message["From"] = email
    message["To"] = destinatario
    message["Subject"] = assunto
    message.attach(MIMEText(corpo, "plain"))

    try:

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(email, password)

        server.sendmail(email, destinatario, message.as_string())
        print("E-mail enviado com sucesso!")

    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

    finally:
        server.quit()

