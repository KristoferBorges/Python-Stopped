distancia = int(input('Qual a distância da sua viagem: '))
if distancia <= 200:
    valorCobrado = distancia * 0.50
    print('O valor cobrado será de: R${}'.format(valorCobrado))
else:
    valorCobrado = distancia * 0.45
    print('O valor cobrado será de: R${}'.format(valorCobrado))
