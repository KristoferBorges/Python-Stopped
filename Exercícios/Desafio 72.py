numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', \
    'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

escolha = -1
while True:
    escolha = int(input('Escolha um número para ver por extenso [0 - 20] '))
    if escolha < 0 or escolha > 20:
        print('Errado!')
    else:
        print(numeros[escolha])
        continuar = str(input('Deseja continuar [S/N]: '))
        if continuar == 'N' or continuar == 'n':
            break
