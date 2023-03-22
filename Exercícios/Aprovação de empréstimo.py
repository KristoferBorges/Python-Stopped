v_casa = float(input('Qual o valor da Casa R$ '))
v_salario = float(input('Qual o seu salário R$ '))
parcelas = int(input('Quantas parcelas: '))
v_parcela = v_casa / parcelas
verificacao = v_salario * 0.3
tempo = parcelas
years = tempo // 12
mouths = tempo % 12

print('\n')
if v_parcela >= verificacao:
    print('Infelizmente o parcelamento foi negado!')
    print('Valor da parcela R${:,.2f} Valor do salário R${:,.2f}'.format(v_parcela, v_salario))
else:
    print('Valor da Casa - R${:,.2f}'.format(v_casa))
    print('Parcelado em - {}x'.format(parcelas))
    print('Valor da Parcela - R${:,.2f}'.format(v_parcela))
    print('Tempo estimado - {} anos e {} meses'.format(years, mouths))
