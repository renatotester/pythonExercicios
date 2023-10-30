from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api/v1/calcule', methods=['POST'])
def calcular_idade():
    data = request.get_json()
    nome = data.get("nome")
    data_nascimento = data.get("data_nascimento")
    
    # Verificar se todos os parâmetros são fornecidos
    if nome is None or data_nascimento is None:
        return jsonify({"msg": "Ambos nome e data_nascimento são obrigatórios"}), 400

    # Validar a data de nascimento
    try:
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    except ValueError:
        return jsonify({"msg": "A data de nascimento deve estar no formato DD/MM/YYYY"}), 400

    # Calcular a idade
    hoje = datetime.now()
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

    return jsonify({"msg": f"{nome}, sua idade é {idade} anos."})

@app.route('/status', methods=['GET'])
def status():
    return ('', 200)

if __name__ == '__main__':
    app.run(debug=True)
