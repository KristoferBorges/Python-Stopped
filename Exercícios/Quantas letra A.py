frase = str(input('Digite uma frase: ')).strip().upper()
letrasA = frase.count("A")
print('Sua frase possui {} vezes a letra (A)'.format(letrasA))
positionFirst = frase.find("A")
positionEnd = frase.rfind("A")
print('A primeira letra foi encontrada na posição: {}'.format(positionFirst))
print('A última letra foi encontrada na posição: {}'.format(positionEnd))


