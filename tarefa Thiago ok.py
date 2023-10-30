from datetime import datetime

def calcular_idade(nome, data_nascimento):
    # Verificar se a data de nascimento está no formato correto
    try:
        data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
    except ValueError:
        return "A data de nascimento deve estar no formato YYYY-MM-DD"

    # Calcular a idade
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

    return f"{nome}, sua idade é {idade} anos."

# Exemplo de uso:
nome = "Thiago"
data_nascimento = "1985-05-22"
mensagem = calcular_idade(nome, data_nascimento)
print(mensagem)
