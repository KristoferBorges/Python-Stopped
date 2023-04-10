print('Cadastro de Pessoas')

stop = "NÃO"
maiores_18 = 0
qnt_homens = 0
qnt_m_idade_menor_20 = 0
while stop == 'NÃO' or stop == 'N':
    # nomes = str(input('Nome: ')).upper().strip()
    idades = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if idades > 18:
        maiores_18 = maiores_18 + 1
    if sexo == 'M':
        qnt_homens = qnt_homens + 1
    if sexo == 'F' and idades < 20:
        qnt_m_idade_menor_20 = qnt_m_idade_menor_20 + 1

    stop = str(input('Deseja Parar? [SIM/NÃO]')).upper().strip()
    print('\n')

print(f'Pessoas com idade maior que 18 anos = {maiores_18}')
print(f'Quantidade de homens = {qnt_homens}')
print(f'Quantidade de mulheres com menos de 20 anos = {qnt_m_idade_menor_20}')
