from flask import request

def GetDate(nome, sobrenome, email, fone):
    file = open("C:\\Users\\callebe.lima\\Documents\\bdtxt\\document.txt", "w")
    file.write(f"{nome};{sobrenome};{email};{fone}\n")
    file.close()
    return "Enviado!"