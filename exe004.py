#faca um progrma que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as informações possíveis sobre ele.
print('Olá Mundo!')
a=input('Digite algo: ')
#O ""a" é o que nós chamamos de objeto.
print('O tipo primitivo desse valor é',type(a))
print('Só tem espaços?',a.isspace())
print('É um número?',a.isnumeric())
print('É alfabético?',a.isalpha())
print('É alfanumérico?',a.isalnum())
print('Está em maiúsculo?',a.isupper())
print('Está em minúscula?',a.islower())
print('Está capitalizada?',a.istitle())