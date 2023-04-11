print('\033[33mCarrinho de Compras')
total = 0
p_acima_1000 = 0
p_mais_barato = 0
cont = 1
stop = ''

while True:
    nomes = str(input('Nome do Produto: ')).strip()
    valor = float(input('Valor do Produto: '))
    total = total + valor
    if valor > 1000:
        p_acima_1000 = p_acima_1000 + 1
    if cont == 1:
        p_mais_barato = nomes
    elif p_mais_barato < valor:
        p_mais_barato = nomes

    stop = str(input('Deseja parar? [SIM/NÃO]: ')).upper().strip()
    if stop == 'S' or stop == 'SIM':
        break
print(f'Valor total gasto = R$ {total}')
print(f'Produtos com o valor acima de R$ 1.000,00 = [{p_acima_1000}]')
print(f'O Produto mais barato foi [{p_mais_barato}]')
