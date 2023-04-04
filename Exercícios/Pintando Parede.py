
height = float(input('Altura: '))
width = float(input('Largura: '))

area = height * width
tinta = area / 2
print('Area de ({:.2f} x {:.2f}) possui ao todo ({:.2f}m²)'.format(height, width, area))
print('Para pintar a parede sera necessario {:.2f}Litros de tinta!'.format(tinta))

