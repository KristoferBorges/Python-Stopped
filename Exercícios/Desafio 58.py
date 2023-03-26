import random

number_choice = random.randint(1, 10)
escolhido = 0
quantidade = 1
while escolhido != number_choice:
    escolhido = int(input('Adivinhe o número que eu estou Pensando: '))
    if escolhido == number_choice:
        print('\033[32mVocê acertou\033[m')
        print('Foram necessários {} jogadas para acertar!'.format(quantidade))
    else:
        if escolhido < number_choice:
            print('Mais...', end=' ')
        elif escolhido > number_choice:
            print('Menos...', end=' ')
        quantidade = quantidade + 1
        print('Tente de novo!\n')
