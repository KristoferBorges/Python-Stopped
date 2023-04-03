from datetime import datetime

ano_atual = datetime.now().year

anos = 0
maiores = 0
menores = 0
for i in range(1, 7+1):
    anos = int(input('Digite seu ano de nascimento {}: '.format(i)))
    if anos <= 2002:
        maiores = maiores + 1
    else:
        menores = menores + 1


print('De menores temos {} pessoas!'.format(menores))
print('De maiores temos {} pessoas!'.format(maiores))
