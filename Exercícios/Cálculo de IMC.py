def calculo(__massa__, __altura__):
    imc = massa / (altura ** 2)
    return imc


massa = float(input('Quando você pesa: '))
altura = float(input('Qual é a sua altura: '))

resultado = calculo(massa, altura)

if resultado < 18.5:
    print('Seu IMC é {:.2f}'.format(resultado))
    print('Você está Abaixo do Peso!')
elif resultado >= 18.5 and resultado < 25:
    print('Seu IMC é {:.2f}'.format(resultado))
    print('Você está no Peso Ideal!')
elif resultado >= 25 and resultado < 30:
    print('Seu IMC é {:.2f}'.format(resultado))
    print('Você está Um pouco Acima do Peso!')
elif resultado >= 30 and resultado < 40:
    print('Seu IMC é {:.2f}'.format(resultado))
    print('Você está Muito Acima do Peso!')
elif resultado > 40:
    print('Seu IMC é {:.2f}'.format(resultado))
    print('Você está na fase de Obesidade Mórbida!')
