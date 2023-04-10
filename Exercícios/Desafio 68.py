import random
import time

print('Jogo Par / Impar')

computer_choice = random.randint(0, 10)
user = True
result = 0
qnt_win = 0
while user:
    print('Impar ou Par [P / I]')
    user_choice = str(input(' --> ')).upper().strip()
    if user_choice == 'P':
        print(f'Você escolheu PAR!')
    elif user_choice == 'I':
        print(f'Você escolheu IMPAR!')
    else:
        print('Resposta Errada!')
    n = int(input('Escolha um número para Jogar: '))
    print(f' Seu número foi {n}')
    print(f' O número do computador foi {computer_choice}')
    print(f'{n} + {computer_choice} = {n + computer_choice}')
    result = n + computer_choice
    if result % 2 == 0:
        print(f'Resultado = PAR!')
        if user_choice == 'P':
            print('Usuário Venceu!')
            qnt_win = qnt_win + 1
            time.sleep(2)
        else:
            print('Usuário Perdeu!')
            break
    else:
        print(f'Resultado = IMPAR')
        if user_choice == 'I':
            print('Usuário Venceu!')
            qnt_win = qnt_win + 1
            time.sleep(2)
        else:
            print('Usuário Perdeu!')
            break

print(f'Usuário Ganhou {qnt_win} vezes!')
