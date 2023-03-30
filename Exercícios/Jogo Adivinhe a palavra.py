
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
normal = '\033[m'

print(yellow + 'JOGO DE ADIVINHA!')
print('Qual será a palavra?' + normal)
palavra = str(input(': ')).strip().upper()
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
dica1 = str(input('Qual será a primeira dica: ')).strip().upper()
dica2 = str(input('Qual será a segunda dica: ')).strip().upper()
print('\n\n\n\n')
for c in range(5, 0, -1):
    escolha = str(input('Faça sua escolha ({}-Vidas): '.format(c))).strip().upper()
    if escolha != palavra:
        print(red + 'Errou!' + normal)
        if c == 1:
            print(red + 'Você perdeu!' + normal)
    else:
        print(green + 'Você Acertou!' + normal)
        break
