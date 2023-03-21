fatura = float(input('Valor da Fatura R$'))
opcao = input('Voce possui um desconto de 5%, deseja utilizar? (Sim/Nao): ')

if opcao == "sim":
    print('Voce aderiu o desconto!')
    novoValor = fatura - (fatura * 5 / 100)
    print('O novo valor da fatura e de R${:,.2f}'.format(novoValor))
else:
    print('Voce nao aderiu o desconto!')
    print('O valor da fatura permanece R${:,.2f}'.format(fatura))
