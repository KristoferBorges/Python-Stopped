def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


numero = int(input('Escolha um número: '))
if primo(numero):
    print('Número primo')
else:
    print('Não é primo')
