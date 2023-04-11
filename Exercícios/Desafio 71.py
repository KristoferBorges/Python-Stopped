print('=' * 30)
print('{:^30}'.format('Banco Negresco'))
print('=' * 30)

valor = int(input('Qual valor do Saque R$ '))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total = total - ced
        totced = totced + 1
    else:
        if totced > 0:
            print('{:^26}'.format(f'Valor = R${ced} | Qnt = {totced}'))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
