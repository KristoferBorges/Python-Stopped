produto = 200.00

print('Formas de pagamento disponíveis: (PIX, Crédito, CréditoParcelado, Débito, Dinheiro e Cheque)')
pagamento = str(input('Escolha a forma de pagamento: ')).strip().lower()

if pagamento == 'créditoparcelado':
    parcelamento = int(input('Quantas parcelas: '))
    if parcelamento <= 2:
        valorTotal = produto
        print('Valor a pagar R${:,.2f} em {}x'.format(valorTotal, parcelamento))
    elif parcelamento > 2:
        valorTotal = produto + (produto * 20 / 100)
        print('Valor a pagar R${:,.2f} em {}x com 20% de juros'.format(valorTotal, parcelamento))
        valorParcela = valorTotal / parcelamento
        print('Cada parcela no valor de R${:,.2f}'.format(valorParcela))
elif pagamento == 'dinheiro' or pagamento == 'débito' or pagamento == 'cheque' or pagamento == 'pix':
    valorTotal = produto - (produto * 10 / 100)
    print('Valor a pagar R${:,.2f} com 10% OFF'.format(valorTotal))
elif pagamento == 'crédito':
    valorTotal = produto - (produto * 5 / 100)
    print('Valor a pagar R${:,.2f} com 5% OFF'.format(valorTotal))
else:
    print('Valor inválido!')
