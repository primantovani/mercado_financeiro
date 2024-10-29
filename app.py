from flask import Flask, render_template, redirect, url_for, request
# declaração da lista de investimentos
from datetime import datetime 

app = Flask(__name__)

# Lista para armazenar os investimentos
investimentos = []

def registrar_investimento(tipo, valor):
    investimento = {
        'tipo': tipo,
        'valor': valor,
        'data': datetime.now() 
    }
    investimentos.append(investimento)
    print("Investimento registrado:", investimento)
    return investimento

# Caminho para a página principal
@app.route('/')
def index():
    return render_template('index.html')

# Caminho para o botão Investir
@app.route('/investir', methods=['POST'])
def investir():
    tipo = request.form.get('tipo')  
    valor = request.form.get('valor')

    try:
        valor = float(valor) 
        novo_investimento = registrar_investimento(tipo, valor)
    except ValueError:
        print("Erro: O valor do investimento não é um número válido.")
        return redirect(url_for('index'))

    return redirect(url_for('index'))

# Caminho para o botão Resgatar
@app.route('/resgatar', methods=['POST'])
def resgatar():
    return "Resgatar acionado!"

# Caminho para o botão Sair
@app.route('/sair', methods=['POST'])
def sair():
    return "Você saiu!"

# Nova rota para listar investimentos
@app.route('/investimentos', methods=['GET'])
def lista_investimentos():
    return render_template('investimentos.html', investimentos=investimentos)

if __name__ == '__main__':
    app.run(debug=True)
