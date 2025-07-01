#faca um progrma que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as informações possíveis sobre ele.
print('Olá Mundo!')
def analisar_entrada():
    """
    Lê uma entrada do usuário e exibe informações detalhadas sobre ela.
    """
    valor = input('Digite algo: ')
    print('-' * 40)
    print(f'O tipo primitivo desse valor é {type(valor)}')
    print(f'Só tem espaços? {valor.isspace()}')
    print(f'É numérico? {valor.isnumeric()}')
    print(f'É alfabético? {valor.isalpha()}')
    print(f'É alfanumérico? {valor.isalnum()}')
    print(f'Está em maiúsculas? {valor.isupper()}')
    print(f'Está em minúsculas? {valor.islower()}')
    print(f'Está capitalizada? {valor.istitle()}')
    print('-' * 40)

if __name__ == "__main__":
    print('Olá, Mundo!')
    analisar_entrada()
