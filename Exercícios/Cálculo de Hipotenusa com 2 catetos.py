import math

cateto1 = int(input('Primeiro cateto: '))
cateto2 = int(input('Segundo cateto: '))
print('\n')

hipotenusa = (math.pow(cateto1, 2)) + (math.pow(cateto2, 2))
resultado = math.sqrt(hipotenusa)
print('Comprimento da Hipotenusa: {}'.format(math.trunc(resultado)))
