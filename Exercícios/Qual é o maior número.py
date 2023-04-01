import random
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

menor = min(n1, n2, n3)
maior = max(n1, n2, n3)

print('O menor número é: {}'.format(menor))
print('O maior número é: {}'.format(maior))
