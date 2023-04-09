# Enunciado
print('Soma entre números!')

# Variáveis
total = 0
maior_n = 0
menor_n = 0
quantidade = 0
escolha = ''

# Laço de Repetição / While
while escolha != 'N':
    number = int(input('Digite um número: '))
    quantidade = quantidade + 1
    total = total + number
    if quantidade == 1:
        maior_n = number
        menor_n = number
    elif number > maior_n:
        maior_n = number
    elif number < menor_n:
        menor_n = number

    print('Deseja continuar: [N/S]')
    escolha = str(input('-->')).upper().strip()

# Finalizar com as informações
print(f'A média entre os número é de {total / quantidade}')
print(f'O maior número foi {maior_n}!')
print(f'O menor número foi {menor_n}!')
