listagem = ('Feijão', 17.60, 'Batata', 4.20, 'Frango', 36.30, 'Abacate', 9.20)

print('=' * 40)
print('{:.^40}'.format('Lista de Produtos'))
print('=' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')


print(f'\033[32m   {usuario}\033[m', end=' ')
        print(f'\033[33mLv {user_level}\033[m X \033[31m{card_monster}\033[m', end=' ')
        print(f'\033[33mLv {lv_monster}\033[m')
        print(f'\033[33m   Power: {power_usuario}\033[m', end='   X')
        print(f'\033[33m  Power: {power_monster}\033[m')
        result()
        print('   --> {:.2f}x'.format(multiplicador))
        print('   --> {} Pontos'.format(point))