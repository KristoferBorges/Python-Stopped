soma = 0
n = 0
print('Somador de números, digite 999 para parar!')
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        soma = soma + n

print(f'O total somado foi de {soma}')
