termo = int(input('Escreva o primeiro termo de uma PA: '))
razao = int(input('Escreva o valor da razão da PA: '))

cont = 1
escolha = 99
termos_extra = 0
while cont <= 10:
    print('{}'.format(termo), end=' ')
    termo = termo + razao
    cont += 1
print('\nDeseja ver outros termos da mesma PA? [S/N]')
escolha = str(input('--> ')).upper().strip()
if escolha == 'S':
    termos_extra = int(input('Quantos termos: '))
    cont = 1
    while cont <= termos_extra:
        print('{}'.format(termo), end=' ')
        termo = termo + razao
        cont += 1
else:
    print('FIM')
