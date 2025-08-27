import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return "Ok", 200

@app.route('/criar', methods=['POST'])
def criar():
    data = request.get_json()
    nome = data.get('nome')
    print(f"Nome recebido: {nome}")
    return "Criar ok", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

