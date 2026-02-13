from flask import Flask
import views

app = Flask(__name__)

# Configuração das rotas
app.add_url_rule("/", view_func=views.home)
app.add_url_rule("/enviar", view_func=views.enviar_dados, methods=['POST'])

if __name__ == "__main__":
    app.run(debug=True)