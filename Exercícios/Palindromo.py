frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')
