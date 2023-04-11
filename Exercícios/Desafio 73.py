times = 'Bahia', 'Jamelão', 'Ringado', 'Chamador', 'Chapecoense', 'Sisco de Ouro', 'Brasil', 'Oeste', 'Tiuve', \
    'Trono', 'Valento', 'Palmeiras', 'São Caetano', 'Urubo', 'Quatorze', 'Wagosto', 'Alemanto', 'Chinasco', \
    'Brililim', 'Dezenove'

localidade = times.index('Chapecoense')

print('-=-' * 30)
print(f'Os cinco primeiros colocados são: {times[:5]}')
print('-=-' * 30)
print(f'Os últimos quatro colocados são: {times[-5:]}')
print('-=-' * 30)
print(f'Em ordem alfabética fica: {sorted(times)}')
print('-=-' * 30)
print(f'O time Chapecoense fica na {localidade}º posição: ')
print('-=-' * 30)
