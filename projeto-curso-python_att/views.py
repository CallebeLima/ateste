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
    flash(GetDate(nome, sobrenome, email, fone))
    return home()

#route sobre
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

#route ref
@app.route("/referencia")
def referencia():
    return render_template("referencia.html")
