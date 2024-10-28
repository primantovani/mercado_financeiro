from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Caminho para a página principal
@app.route('/')
def index():
    return render_template('index.html')

# Caminho para o botão Investir
@app.route('/investir', methods=['POST'])
def investir():
    return "Investir acionado!"

# Caminho para o botão Resgatar
@app.route('/resgatar', methods=['POST'])
def resgatar():
    return "Resgatar acionado!"

# Caminho para o botão Sair
@app.route('/sair', methods=['POST'])
def sair():
    return "Você saiu!"

if __name__ == '__main__':
    app.run(debug=True)
