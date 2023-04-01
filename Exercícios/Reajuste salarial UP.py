class Pessoa():
        
    salario = float
    while salario != 0:
            salario = float(input('Informe seu salario: '))
            if salario == 15000:
                print('Seu cargo e de Diretor!')
                novoSalario = salario + (salario * 5 / 100)
                print('Seu Salario teve um aumento de 5%')
                print('NOVO SALARIO R${}\n'.format(novoSalario))
            elif salario == 8000:
                print('Seu cargo e de Coordenador!')
                novoSalario = salario + (salario * 15 / 100)
                print('Seu Salario teve um aumento de 15%')
                print('NOVO SALARIO R${}\n'.format(novoSalario))
            elif salario == 1200:
                print('Seu cargo e de Operador!')
                novoSalario = salario + (salario * 20 / 100)
                print('Seu Salario teve um aumento de 20%')
                print('NOVO SALARIO R${}\n'.format(novoSalario))
            elif salario == 0:
                print('Saindo do programa!\n')
            else:
                print('Digite um valor valido!\n')
