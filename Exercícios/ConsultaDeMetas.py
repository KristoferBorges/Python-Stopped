import sys
import time

# Cores
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
ciano = '\033[36m'
normal = '\033[m'
roxo = '\033[35m'
rosa = '\033[95m'

titulo = "CONSULTA DE METAS"
tamanho = 43
titulo_centralizado = titulo.center(tamanho)

texto_dados = "DADOS ARMAZENADOS!"
texto_dados_centralizado = texto_dados.center(tamanho)

print(rosa + '$=' * 21 + normal)
print(roxo + titulo_centralizado + normal)
print(rosa + '$=' * 21 + normal)
print('\n')

# input de decisão
decis = str(input(red + ' [?] - Deseja Limpar os dados atuais? [S/N] ' + normal)).upper().strip()
if decis == 'S':
    confirmacao = str(input(red + ' [!] - Confirme a exclusao dos dados [S/N] ' + normal)).upper().strip()
    if confirmacao == 'S':
        with open("dados.txt", "w") as dados:
            dados.write("DATA---------------META-------------META.AC---------VENDAS----------VENDAS.AC-----P---------")
        with open("metaAcumulada.txt", "w") as metaAcumulada:
            metaAcumulada.write("")
        with open("vendaAcumulada.txt", "w") as vendaAcumulada:
            vendaAcumulada.write("")
        for i in range(3, 0, -1):
            time.sleep(0.6)
            print(red, end='')
            print(f' [!] - CARREGANDO [{i}]')
            print(normal, end='')
        print(green + ' [!] - PROCESSO FINALIZADO')
        sys.exit()
    elif confirmacao != 'S':
        print('\n' + red + ' [!] - PROCESSO INTERROMPIDO')

else:
    print(green + ' [!] - SISTEMA DE REGISTRO\n' + normal)
    # Inputs de dados
    data = str(input(green + ' [?] - Informe a data [dia/mês/ano]: '))
    metaDia = float(input(' [?] - Qual a Meta do Dia R$ '))
    vendaDia = float(input(' [?] - Quando Vendeu Hoje R$ '))
    print(normal)
    metaAc = 0
    vendaAc = 0
    porcentagem = 0

    # Cálculo de Metas acumuladas
    with open("metaAcumulada.txt", "a") as metaAcumulada:
        metaAcumulada.write(f"{metaDia}\n")
    with open("metaAcumulada.txt", "r") as metaAcumulada:
        linhas = metaAcumulada.readlines()

    for linha in linhas:
        metaAc = metaAc + float(linha.strip())
    print(yellow + f" [!] - META ACUMULADA = ", end='')
    print(rosa + f"R$ {metaAc:.2f}" + normal)

    # Cálculo de Vendas acumuladas
    with open("vendaAcumulada.txt", "a") as vendaAcumulada:
        vendaAcumulada.write(f"{vendaDia}\n")
    with open("vendaAcumulada.txt", "r") as vendaAcumulada:
        linhas2 = vendaAcumulada.readlines()

    for linha in linhas2:
        vendaAc = vendaAc + float(linha.strip())
    print(yellow + f" [!] - VENDA ACUMULADA = ", end='')
    print(rosa + f"R$ {vendaAc:.2f}" + normal)

    # Cálculo de porcentagem
    porcentagem = (vendaAc / metaAc) * 100
    print(yellow + f" [!] - PORCENTAGEM ACUMULADA = ", end='')
    print(rosa + f"{porcentagem:.2f}%" + normal)
    print('\n')
    print(rosa + '=-' * 21 + normal)
    print(roxo + texto_dados_centralizado + normal)
    print(rosa + '=-' * 21 + normal)
    # Inserção de dados
    with open("dados.txt", "a") as dados:
        dados.write(f"{data}  |  R${metaDia:.2f}  |  R${metaAc:.2f}  |  R${vendaDia:.2f}  |  R${vendaAc:.2f}  |  "
                    f"{porcentagem:.2f}%\n")