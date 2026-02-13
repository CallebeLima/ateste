from flask import render_template, request
from readtext import ProcessarAta
from time import sleep

participantes = []

def home():
    return render_template("home.html")

def error():
    return render_template("erro.html")

def _sucesso():
    return render_template("sucesso.html")

def enviar_dados():
    titulo = request.form.get('titulo')
    participantes.append(request.form.get('participantes'))
    data = request.form.get('data')
    assuntos = request.form.get('assuntos')
    acoes = request.form.get('acoes')
    
    sucesso = ProcessarAta(titulo, participantes, data, assuntos, acoes)
    
    if sucesso:
        titulo = ''
        participantes.clear()
        data =''
        assuntos = ''
        acoes = ''
        return _sucesso()
    titulo = ''
    participantes.clear()
    data =''
    assuntos = ''
    acoes = ''         
    return error()