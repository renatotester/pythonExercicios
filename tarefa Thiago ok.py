#criar uma api que calcule a idade
# -> POST /api/v1/calcule
#"nome": <string>,
#			"data_nascimento": <string>			
#		}
#		- validar entradas
#		- todos os parametros sao obrigatorios
#		- retorno:
#			{
#				"msg": "<nome> sua idade é <idade>"	
#			}
#					
#-> /status
#- sempre retorna 200 e nao retorna conteudo
#	curl -x POST 127.0.0.1:5000/api/v1/calcule -d '{"nome":"thiago","data_nascimento":"22/05/1985"}'

#importando datetime
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
