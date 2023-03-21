from datetime import datetime
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

data = datetime.now().year
sexo = str(input('Qual seu sexo Masculino ou Feminino: ')).lower()
if sexo == 'feminino':
    print(cyan + 'Você não precisa se Alistar!' + normal)
    sys.exit()
nascimento = int(input('Em qual ano você nasceu: '))
idade = data - nascimento


if idade < 18:
    tempo = 18 - idade
    print('\033[36mVocê precisa de alistar daqui {} ano(s)\033[m'.format(tempo))
elif nascimento < 1850:
    print('\033[34mError\033[m')
elif idade > 18:
    tempo = idade - 18
    print('\033[36mTempo de alistamento ultrapassado em {} ano(s)\033[m'.format(tempo))
elif idade == 18:
    print('\033[36mVocê precisa se alistar ainda nesse ano!\033[m')
