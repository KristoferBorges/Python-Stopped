termo = int(input('Escreva o primeiro termo de uma PA: '))
razao = int(input('Escreva o valor da razão da PA: '))

cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' > ')
    termo = termo + razao
    cont += 1

print('FIM')
    