n1 = int(input('Digite um Número: '))
n2 = int(input('Digite outro Número: '))

print('Você poderá realizar as seguintes operações!')
print('Caso queira sair do programa, aperte 0')
print(' \033[35m(1) - Somar')
print(' (2) - Multiplicar')
print(' (3) - Maior')
print(' (4) - Novo números')
print(' (5) - Sair do Programa\033[m')
digitado = 99
while digitado != 0:
    digitado = float(input('OP --> '))
    if digitado == 1:
        result = n1 + n2
        print(f'Resultado entre {n1} + {n2} = ({result})')
    elif digitado == 2:
        result = n1 * n2
        print(f'Resultado - ({result})')
    elif digitado == 3:
        if n1 > n2:
            result = n1
        else:
            result = n2
        print(f'Resultado do Maior número digitado - ({result})')
    elif digitado == 4:
        n1 = float(input('Digite um Número: '))
        n2 = float(input('Digite outro Número: '))
    elif digitado == 5:
        print('Finalizado')
