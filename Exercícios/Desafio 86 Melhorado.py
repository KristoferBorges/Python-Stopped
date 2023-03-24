"""
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos
pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = list()
totalpares = 0
coluna3 = 0
line2_maxValue = 0
for li in range(0, 3):
    for co in range(0, 3):
        matriz[li][co] = int(input(f'Digite um valor para a posição {[li]}{[co]}'))
        if matriz[li][co] % 2 == 0:
            pares.append(matriz[li][co])

for n in pares:
    totalpares = totalpares + n

coluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]

print('-=-' * 20)
for li in range(0, 3):
    for co in range(0, 3):
        print(f'[{matriz[li][co]:^5}]', end='')
    print()

if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
    line2_maxValue = matriz[1][0]
elif matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
    line2_maxValue = matriz[1][1]
elif matriz[1][2] > matriz[1][0] and matriz[1][1]:
    line2_maxValue = matriz[1][2]

print('-=-' * 20)
print(f'Números pares: {pares} = {totalpares}')
print(f'Soma dos números (3ºColuna) = {coluna3}')
print(f'O maior valor da (2ºLinha) = {line2_maxValue}')
