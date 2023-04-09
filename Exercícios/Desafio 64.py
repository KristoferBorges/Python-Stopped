quantidade = 0
total = 0
number = 0
print('Sistema de contador de números!\n')
while number != 999:
    number = int(input('Digite um número\nCaso queira para digite [999]: '))
    total = total + number
    quantidade = quantidade + 1
    if number == 999:
        quantidade = quantidade - 1
        total = total - 999


print('A quantidade de números digitados foram ({}) e o total somado é ({})'.format(quantidade, total))
