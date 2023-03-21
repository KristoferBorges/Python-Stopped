dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos KM foram percorridos: '))
print('\n')

valorDia = dias * 60
valorKm = km * 0.15

valorTotal = valorDia + valorKm
print('| Total a pagar R${:,.2f} \n'.format(valorTotal))
