import sys

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
normal = "\033[0m"

nota1 = float(input('Nota de Português: '))
nota2 = float(input('Nota de Matemática: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(media)
    print('REPROVADO')
elif media >= 5.0 and media < 7:
    print(media)
    print('RECUPERAÇÃO')
elif media >= 7:
    print(media)
    print('APROVADO')
sys.exit()
