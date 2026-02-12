from main import app
from flask import render_template, request, flash
from readtext import *

#route inicio
@app.route("/")
def home():
    return render_template("home.html")

# Route para receber os dados
@app.route("/enviar", methods=['GET','POST'])
def enviar_dados():
    nome = request.form.get('nome_input')
    sobrenome = request.form.get('snome_input')
    email = request.form.get('email_input')
    fone = request.form.get('fone_input')
    
    return '''<div id="Alert" style="    position: fixed;
    border: 1px solid rgb(234, 8, 8);
    background-color: rgb(255, 184, 184);
    border-radius: 10px;
    left: 38%;
    display: flex;
    flex-direction: row;
    width: 350px;
    height: 40px;    
    padding: 20px;
    gap: 10px;
    margin: 0 auto 0 auto;
    align-items: center;
    justify-content: center;">
      <div id="emoji" style="    display: flex;
    align-items: center;" >❌</div>
      <div id="message">
        <h1>Dados Inválidos</h1>
        <p>Preencha corretamente os dados.</p>
      </div>'''
    
    GetDate(nome, sobrenome, email, fone)
    
    return home()

#route sobre
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

#route ref
@app.route("/referencia")
def referencia():
    return render_template("referencia.html")
