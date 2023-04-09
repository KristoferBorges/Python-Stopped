print('Escolha um número para ver sua tabuada\nCaso queira para digite um número negativo!')

n = 0
cont = 0

while True:
    print('\n')
    n = int(input('Digite um número: '))
    if n <= 0:
        break
    for i in range(0, 10 + 1):
        print(f'{n} x {i} = {n * i}')
        cont = cont + 1

print('FIM')
