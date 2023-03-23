n1 = int(input('Número um: '))
n2 = int(input('Número dois: '))

if n1 > n2:
    print('O Número {} é maior que o Número {}'.format(n1, n2))
elif n1 < n2:
    print('O Número {} é maior que o Número {}'.format(n2, n1))
else:
    print('Os dois Números são iguais!')
