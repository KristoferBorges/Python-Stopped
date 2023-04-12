numberx9 = 0
positionx3 = 0
numbersxPares = 0

numbers = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), \
    int(input('Digite um número: '))

print(numbers)
print('\n')
print(f'O número 9 aparece {numbers.count(9)}x')
if numbers == 3:
    print(f'O Número 3 foi visto na {numbers.index(3) + 1}º posição')
else:
    print('Os números pares são: ', end=' ')
for c in numbers:
    if c % 2 == 0:
        print(c, end=' ')
