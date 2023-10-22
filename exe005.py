#operações matemáticas - operadores aritiméticos
#todo operador precisa de um operando (pode ser um número ou pode ser uma string.
# "+" - adição
# "-" - subtração
# "*" - multiplicação
# "/" - divisão
#########################
# "**" - potência
# "//" - divisão inteira
# "%" - não é usado para porcentagem normal e sim para o resto da divisão

print('Olá Mundo!')
#quando eu quero testar se duas coisas são iguais eu uso igual duplo "=="
#ordem de precedênci (1(), 2**, 3*,/,//,%, 4 +,-.
#5+2==7
#5-2==3
#5*2==10
#5/2==2.5
#5**2==25
#5//2==2
#5%2==1

n1=int(input('Um valor:'))
n2=int(input('Outro valor:'))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
#, o produto é {} e a divisão é{:.3f}'.format(s,m,d))
print('A soma é {},' .format(s))
print('O produto é {}'.format(m))
print('A divisão é {:.2f}'.format(d))
print('A divisão inteira é {:.2f}'.format(di))
print('A potência é {}'.format(e))

#print('Divisão inteira {} e potência {}'.format(di, e))