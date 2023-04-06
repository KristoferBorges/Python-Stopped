print('\n')
vel = int(input('Em qual velocidade foi visto o veículo em Km/h\n--> '))
multa = (vel - 80) * 7.00
if vel > 80:
    print('Por excesso de velocidade você foi multado!')
    print('VELOCIDADE MÁXIMA = 80km/h')
    print('VELOCIDADE DO VEÍCULO = {}km/h'.format(vel))
    print('VALOR COBRADO: R${:,.2f}'.format(multa))
else:
    print('Velocidade não excedida!')
