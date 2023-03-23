real = float(input('Quantos reais deseja converter R$ '))
dolar = real / 5.31

print('Com R${:,.2f} voce pode ter U${:,.2f}'.format(real, dolar))
