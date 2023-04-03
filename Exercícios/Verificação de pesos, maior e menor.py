menor = 0
maior = 0

for i in range(1, 5+1):
    peso = float(input('Qual seu peso {}: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('O maior é {}Kg'.format(maior))
print(f'O menor é {menor}Kg')
