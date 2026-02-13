import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def ProcessarAta(titulo, participantes, data, assuntos, acoes):
    # 1. SALVAMENTO LOCAL (Backup em TXT)
    caminho = r"C:\\Users\\aluno\\Documents\\atas_reuniao.txt"
    
    try:
        with open(caminho, "a", encoding="utf-8") as file:
            file.write(f"\n{'='*50}\nREUNIÃO: {titulo} | DATA: {data}\n")
            file.write(f"PARTICIPANTES: {participantes}\n")
            file.write(f"DISCUSSÃO: {assuntos}\nAÇÕES: {acoes}\n{'='*50}\n")
        
        # 2. DISPARO DO BOT DE EMAIL
        enviar_email_ata(titulo, participantes, data, assuntos, acoes)
        
        return True
    except Exception as e:
        print(f"Erro no sistema: {e}")
        return False

def enviar_email_ata(titulo, participantes, data, assuntos, acoes):
    # Configurações do seu bot (Use Senha de Aplicativo do Google)
    meu_email = "callebelima96@gmail.com"
    minha_senha = "fbge fmnv wrly eyry" # Aquela de 16 dígitos
    destino = participantes[0]
    destino_geral = ''
    for i in participantes:
        destino_geral += f'{i}'
    corpoEmail = ''
    participantes_listas = participantes[0].split(",")
    for participantes in participantes_listas:
        formato_participantes = participantes.split("@")
        corpoEmail += f'{formato_participantes[0]}\n'
    msg = MIMEMultipart()
    msg['From'] = meu_email
    msg['To'] = destino
    msg['Subject'] = f"📝 Ata de Reunião: {titulo}"

    corpo_email = f"""
    Segue o registro da reunião:
    
    TÍTULO: {titulo}
    DATA: {data}
    PARTICIPANTES: {corpoEmail}
    
    ASSUNTOS:
    {assuntos}
    
    AÇÕES DEFINIDAS:
    {acoes}
    
    --- 
    Mensagem enviada automaticamente pelo Minute Maker.
    """
    
    msg.attach(MIMEText(corpo_email, 'plain'))

    try:
        for participantes in participantes_listas:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(meu_email, minha_senha)        
            server.sendmail(meu_email, participantes, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Falha no bot de email: {e}")