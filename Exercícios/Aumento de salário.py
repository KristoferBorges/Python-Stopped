salario = float(input('Qual o seu salário: '))

if salario < 1249.99:
    novoSalario = salario + (salario * 15 / 100)
    print('Seu novo salário será de R${}'.format(novoSalario))
else:
    novoSalario = salario + (salario * 10 / 100)
    print('Seu novo salário será de R${}'.format(novoSalario))
