from datetime import datetime

ano_atual = datetime.now().year
nascimento = int(input('Em qual ano você nasceu: '))
idade = ano_atual - nascimento

if idade <= 9:
    print('Você tem {} anos, sua categoria será Mirim!'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos, sua categoria será Infantil!'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos, sua categoria será Junior!'.format(idade))
elif idade > 19 and idade <= 20:
    print('Você tem {} anos, sua categoria será Sénior!'.format(idade))
elif idade > 20:
    print('Você tem {} anos, sua categoria será MASTER!'.format(idade))




