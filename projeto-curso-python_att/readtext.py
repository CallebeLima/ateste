from flask import request

def GetDate(nome, sobrenome, email, fone):
    if nome == '' or sobrenome == '' or email == '' or fone == '':  
        return "Dados não enviados!"
    try:
        with open('nome_do_arquivo', 'a') as f:
            file = open("C:\\Users\\aluno\\Documents\\save.txt", "a")
            file.write(f"{nome};{sobrenome};{email};{fone}\n")
            file.close()
    except:
        file = open("C:\\Users\\aluno\\Documents\\save.txt", "w")
        file.write(f"{nome};{sobrenome};{email};{fone}\n")
        file.close()
    return "Enviado!"