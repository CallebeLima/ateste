from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return 'Olá mundo!'

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        dados= request.form['name']
        return f'voce enviou: {dados}'
    return '''<form method = "POST">
                nome: <input type ="Text" name ="name">
                <input type ="Submit" value ="Enviar">
              </form>'''
              
@app.route('/tamplate')
def template():
    return render_template('home.html')
    
if __name__ == '__main__':
    app.run(debug=True, port=5152)