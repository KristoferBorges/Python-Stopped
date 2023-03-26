digitado = ''
while digitado != 'M' and digitado != 'F':
    digitado = str(input('Digite seu Sexo: ')).upper()
    if digitado == 'M' or digitado == 'F':
        print('Obrigado!')
    else:
        print('Tente novamente')
        