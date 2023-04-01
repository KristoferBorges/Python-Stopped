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
tamanho_lista = 84
titulo_centralizado = titulo.center(tamanho)

texto_dados = "DADOS ARMAZENADOS!"
texto_dados_centralizado = texto_dados.center(tamanho)

texto_decis = "-DIGITE O NÚMERO CORRESPONDENTE-"
texto_decis_centralizado = texto_decis.center(tamanho)

texto_RDMarcas = roxo + "-LISTA DE RD MARCAS-" + normal
texto_RDMarcas_centralizado = texto_RDMarcas.center(tamanho)

texto_PERFUMARIA = roxo + "-LISTA DE PERFUMARIA-" + normal
texto_PERFUMARIA_centralizado = texto_PERFUMARIA.center(tamanho)

texto_DERMO = roxo + "-LISTA DE DERMO-" + normal
texto_DERMO_centralizado = texto_DERMO.center(tamanho)

texto_RDMarcas_lista_centralizado = texto_RDMarcas.center(tamanho_lista)
texto_PERFUMARIA_lista_centralizado = texto_PERFUMARIA.center(tamanho_lista)
texto_DERMO_lista_centralizado = texto_DERMO.center(tamanho_lista)

print(rosa + '$=' * 21 + normal)
print(roxo + titulo_centralizado + normal)
print(rosa + '$=' * 21 + normal)
print('\n')

# input de decisão
print(texto_decis_centralizado)
decis_registro_exclusao_consulta = int(input(yellow + ' [?] - NOVOS REGISTROS [1]\n'
                                                      ' [?] - LIMPAR DADOS ATUAIS [2]\n'
                                                      ' [?] - CONSULTAR LISTAS ATUAIS [3]\n --> ' + normal))
if decis_registro_exclusao_consulta == 2:
    print('\n')
    print(red + ' [!] - SISTEMA DE EXCLUSÃO\n' + normal)
    print(texto_decis_centralizado)
    decis2_listas = int(input(red + ' [?] - Lista de RD Marcas - [1]\n'
                                    ' [?] - Lista de Perfumaria - [2]\n'
                                    ' [?] - Lista de Dermo [3]\n'
                                    ' --> ' + normal + ''))
    print('\n')
    if decis2_listas == 1:
        confirmacao = str(input(red + ' [!] - Confirme a exclusao dos dados [S/N] ' + normal)).upper().strip()
        if confirmacao == 'S':
            # Exclusão RD MARCAS
            with open("listaRDMARCAS.txt", "w") as listaRDMARCAS:
                listaRDMARCAS.write("DATA-------- META-------- META.AC----- VENDAS----- VENDAS.AC----- P---------\n")
            with open("storage/metaAcumuladaRDMARCAS.txt", "w") as metaAcumuladaRDMARCAS:
                metaAcumuladaRDMARCAS.write("")
            with open("storage/vendaAcumuladaRDMARCAS.txt", "w") as vendaAcumuladaRDMARCAS:
                vendaAcumuladaRDMARCAS.write("")
            for i in range(3, 0, -1):
                time.sleep(0.6)
                print(red, end='')
                print(f' [!] - CARREGANDO {i}')
                print(normal, end='')
            print(green + ' [!] - PROCESSO FINALIZADO')
            sys.exit()
        elif confirmacao != 'S':
            print('\n' + red + ' [!] - PROCESSO INTERROMPIDO')
    elif decis2_listas == 2:
        # Exclusão Perfumaria
        confirmacao = str(input(red + ' [!] - Confirme a exclusao dos dados [S/N] ' + normal)).upper().strip()
        if confirmacao == 'S':
            with open("listaPERFUMARIA.txt", "w") as listaPERFUMARIA:
                listaPERFUMARIA.write("DATA-------- META-------- META.AC----- VENDAS----- VENDAS.AC----- P---------\n")
            with open("storage/metaAcumuladaPERFUMARIA.txt", "w") as metaAcumuladaPERFUMARIA:
                metaAcumuladaPERFUMARIA.write("")
            with open("storage/vendaAcumuladaPERFUMARIA.txt", "w") as vendaAcumuladaPERFUMARIA:
                vendaAcumuladaPERFUMARIA.write("")
            for i in range(3, 0, -1):
                time.sleep(0.6)
                print(red, end='')
                print(f' [!] - CARREGANDO {i}')
                print(normal, end='')
            print(green + ' [!] - PROCESSO FINALIZADO')
            sys.exit()
        elif confirmacao != 'S':
            print('\n' + red + ' [!] - PROCESSO INTERROMPIDO')
    elif decis2_listas == 3:
        # Exclusão Dermo
        confirmacao = str(input(red + ' [!] - Confirme a exclusao dos dados [S/N] ' + normal)).upper().strip()
        if confirmacao == 'S':
            with open("listaDERMO.txt", "w") as listaDERMO:
                listaDERMO.write("DATA-------- META-------- META.AC----- VENDAS----- VENDAS.AC----- P---------\n")
            with open("storage/metaAcumuladaDERMO.txt", "w") as metaAcumuladaDERMO:
                metaAcumuladaDERMO.write("")
            with open("storage/vendaAcumuladaDERMO.txt", "w") as vendaAcumuladaDERMO:
                vendaAcumuladaDERMO.write("")
            for i in range(3, 0, -1):
                time.sleep(0.6)
                print(red, end='')
                print(f' [!] - CARREGANDO {i}')
                print(normal, end='')
            print(green + ' [!] - PROCESSO FINALIZADO')
            sys.exit()
        elif confirmacao != 'S':
            print('\n' + red + ' [!] - PROCESSO INTERROMPIDO')
elif decis_registro_exclusao_consulta == 1:
    print('\n')
    print(green + ' [!] - SISTEMA DE REGISTRO\n' + normal)

    print(texto_decis_centralizado)
    decis_listas = int(input(yellow + ' [?] - Lista de RD Marcas - [1]\n'
                                      ' [?] - Lista de Perfumaria - [2]\n'
                                      ' [?] - Lista de Dermo - [3]\n'
                                      ' --> ' + normal))
    if decis_listas == 1:
        # Inputs de dados - RD Marcas
        print('\n')
        print(texto_RDMarcas_centralizado)
        data = str(input(green + ' [?] - Informe a data [dia/mês/ano]: '))
        metaDia = float(input(' [?] - Qual a Meta do Dia R$ '))
        vendaDia = float(input(' [?] - Quando Vendeu Hoje R$ '))
        print(normal)
        metaAcRDMARCAS = 0
        vendaAcRDMARCAS = 0
        porcentagemRDMARCAS = 0

        # Cálculo de Metas acumuladas
        with open("storage/metaAcumuladaRDMARCAS.txt", "a") as metaAcumuladaRDMARCAS:
            metaAcumuladaRDMARCAS.write(f"{metaDia}\n")
        with open("storage/metaAcumuladaRDMARCAS.txt", "r") as metaAcumuladaRDMARCAS:
            linhas = metaAcumuladaRDMARCAS.readlines()

        for linha in linhas:
            metaAcRDMARCAS = metaAcRDMARCAS + float(linha.strip())
        print(yellow + f" [!] - META ACUMULADA = ", end='')
        print(rosa + f"R$ {metaAcRDMARCAS:.2f}" + normal)

        # Cálculo de Vendas acumuladas
        with open("storage/vendaAcumuladaRDMARCAS.txt", "a") as vendaAcumuladaRDMARCAS:
            vendaAcumuladaRDMARCAS.write(f"{vendaDia}\n")
        with open("storage/vendaAcumuladaRDMARCAS.txt", "r") as vendaAcumuladaRDMARCAS:
            linhas2 = vendaAcumuladaRDMARCAS.readlines()

        for linha in linhas2:
            vendaAcRDMARCAS = vendaAcRDMARCAS + float(linha.strip())
        print(yellow + f" [!] - VENDA ACUMULADA = ", end='')
        print(rosa + f"R$ {vendaAcRDMARCAS:.2f}" + normal)

        # Cálculo de porcentagem
        porcentagemRDMARCAS = (vendaAcRDMARCAS / metaAcRDMARCAS) * 100
        print(yellow + f" [!] - PORCENTAGEM ACUMULADA = ", end='')
        print(rosa + f"{porcentagemRDMARCAS:.2f}%" + normal)
        print('\n')
        print(rosa + '=-' * 21 + normal)
        print(roxo + texto_dados_centralizado + normal)
        print(rosa + '=-' * 21 + normal)
        # Inserção de dados
        with open("listaRDMARCAS.txt", "a") as listaRDMARCAS:
            listaRDMARCAS.write(f"{data} | R${metaDia:.2f} | R${metaAcRDMARCAS:.2f} | R${vendaDia:.2f} |"
                                f" R${vendaAcRDMARCAS:.2f} | "
                                f"{porcentagemRDMARCAS:.2f}%\n")
    elif decis_listas == 2:
        # Inputs de dados - RD Perfumaria
        print('\n')
        print(texto_PERFUMARIA_centralizado)
        data = str(input(green + ' [?] - Informe a data [dia/mês/ano]: '))
        metaDia = float(input(' [?] - Qual a Meta do Dia R$ '))
        vendaDia = float(input(' [?] - Quando Vendeu Hoje R$ '))
        print(normal)
        metaAcPERFUMARIA = 0
        vendaAcPERFUMARIA = 0
        porcentagemPERFUMARIA = 0

        # Cálculo de Metas acumuladas
        with open("storage/metaAcumuladaPERFUMARIA.txt", "a") as metaAcumuladaPERFUMARIA:
            metaAcumuladaPERFUMARIA.write(f"{metaDia}\n")
        with open("storage/metaAcumuladaPERFUMARIA.txt", "r") as metaAcumuladaPERFUMARIA:
            linhas = metaAcumuladaPERFUMARIA.readlines()

        for linha in linhas:
            metaAcPERFUMARIA = metaAcPERFUMARIA + float(linha.strip())
        print(yellow + f" [!] - META ACUMULADA = ", end='')
        print(rosa + f"R$ {metaAcPERFUMARIA:.2f}" + normal)

        # Cálculo de Vendas acumuladas
        with open("storage/vendaAcumuladaPERFUMARIA.txt", "a") as vendaAcumuladaPERFUMARIA:
            vendaAcumuladaPERFUMARIA.write(f"{vendaDia}\n")
        with open("storage/vendaAcumuladaPERFUMARIA.txt", "r") as vendaAcumuladaPERFUMARIA:
            linhas2 = vendaAcumuladaPERFUMARIA.readlines()

        for linha in linhas2:
            vendaAcPERFUMARIA = vendaAcPERFUMARIA + float(linha.strip())
        print(yellow + f" [!] - VENDA ACUMULADA = ", end='')
        print(rosa + f"R$ {vendaAcPERFUMARIA:.2f}" + normal)

        # Cálculo de porcentagem
        porcentagemPERFUMARIA = (vendaAcPERFUMARIA / metaAcPERFUMARIA) * 100
        print(yellow + f" [!] - PORCENTAGEM ACUMULADA = ", end='')
        print(rosa + f"{porcentagemPERFUMARIA:.2f}%" + normal)
        print('\n')
        print(rosa + '=-' * 21 + normal)
        print(roxo + texto_dados_centralizado + normal)
        print(rosa + '=-' * 21 + normal)
        # Inserção de dados
        with open("listaPERFUMARIA.txt", "a") as listaPERFUMARIA:
            listaPERFUMARIA.write(f"{data} | R${metaDia:.2f} | R${metaAcPERFUMARIA:.2f} | R${vendaDia:.2f} |"
                                  f" R${vendaAcPERFUMARIA:.2f} | "
                                  f"{porcentagemPERFUMARIA:.2f}%\n")
    elif decis_listas == 3:
        # Inputs de dados - RD Dermo
        print('\n')
        print(texto_DERMO_centralizado)
        data = str(input(green + ' [?] - Informe a data [dia/mês/ano]: '))
        metaDia = float(input(' [?] - Qual a Meta do Dia R$ '))
        vendaDia = float(input(' [?] - Quando Vendeu Hoje R$ '))
        print(normal)
        metaAcDERMO = 0
        vendaAcDERMO = 0
        porcentagemDERMO = 0

        # Cálculo de Metas acumuladas
        with open("storage/metaAcumuladaDERMO.txt", "a") as metaAcumuladaDERMO:
            metaAcumuladaDERMO.write(f"{metaDia}\n")
        with open("storage/metaAcumuladaDERMO.txt", "r") as metaAcumuladaDERMO:
            linhas = metaAcumuladaDERMO.readlines()

        for linha in linhas:
            metaAcDERMO = metaAcDERMO + float(linha.strip())
        print(yellow + f" [!] - META ACUMULADA = ", end='')
        print(rosa + f"R$ {metaAcDERMO:.2f}" + normal)

        # Cálculo de Vendas acumuladas
        with open("storage/vendaAcumuladaDERMO.txt", "a") as vendaAcumuladaDERMO:
            vendaAcumuladaDERMO.write(f"{vendaDia}\n")
        with open("storage/vendaAcumuladaDERMO.txt", "r") as vendaAcumuladaDERMO:
            linhas2 = vendaAcumuladaDERMO.readlines()

        for linha in linhas2:
            vendaAcDERMO = vendaAcDERMO + float(linha.strip())
        print(yellow + f" [!] - VENDA ACUMULADA = ", end='')
        print(rosa + f"R$ {vendaAcDERMO:.2f}" + normal)

        # Cálculo de porcentagem
        porcentagemDERMO = (vendaAcDERMO / metaAcDERMO) * 100
        print(yellow + f" [!] - PORCENTAGEM ACUMULADA = ", end='')
        print(rosa + f"{porcentagemDERMO:.2f}%" + normal)
        print('\n')
        print(rosa + '=-' * 21 + normal)
        print(roxo + texto_dados_centralizado + normal)
        print(rosa + '=-' * 21 + normal)
        # Inserção de dados
        with open("listaDERMO.txt", "a") as listaDERMO:
            listaDERMO.write(f"{data} | R${metaDia:.2f} | R${metaAcDERMO:.2f} | R${vendaDia:.2f} |"
                             f" R${vendaAcDERMO:.2f} | "
                             f"{porcentagemDERMO:.2f}%\n")
elif decis_registro_exclusao_consulta == 3:
    print('\n')
    print(texto_decis_centralizado)
    decis_consulta = int(input((yellow + " [?] - CONSULTAR LISTA DE RD MARCAS [1]\n"
                                         " [?] - CONSULTAR LISTA DE PERFUMARIA [2]\n"
                                         " [?] - CONSULTAR LISTA DE DERMO [3]\n"
                                         " [?] - CONSULTAR TODAS AS LISTAS [4]\n --> " + normal)))
    if decis_consulta == 1:
        print('¨¨' * 38)
        print(texto_RDMarcas_lista_centralizado)
        with open("listaRDMARCAS.txt", "r") as listaRDMARCAS:
            linhas3 = listaRDMARCAS.readlines()
        for linha in linhas3:
            print(green + f'{linha.strip()}' + normal)
        print('¨¨' * 38)
    elif decis_consulta == 2:
        print('¨¨' * 38)
        print(texto_PERFUMARIA_lista_centralizado)
        with open("listaPERFUMARIA.txt", "r") as listaPERFUMARIA:
            linhas3 = listaPERFUMARIA.readlines()
        for linha in linhas3:
            print(green + f'{linha.strip()}' + normal)
        print('¨¨' * 38)
    elif decis_consulta == 3:
        print('¨¨' * 38)
        print(texto_DERMO_lista_centralizado)
        with open("listaDERMO.txt", "r") as listaDERMO:
            linhas3 = listaDERMO.readlines()
        for linha in linhas3:
            print(green + f'{linha.strip()}' + normal)
        print('¨¨' * 38)
    elif decis_consulta == 4:
        print('¨¨' * 38)
        print('¨¨' * 38)
        print(texto_RDMarcas_lista_centralizado)
        with open("listaRDMARCAS.txt", "r") as listaRDMARCAS:
            linhas3 = listaRDMARCAS.readlines()
        for linha in linhas3:
            print(green + f'{linha.strip()}' + normal)
        print('¨¨' * 38)
        print('¨¨' * 38)
        print(texto_PERFUMARIA_lista_centralizado)
        with open("listaPERFUMARIA.txt", "r") as listaPERFUMARIA:
            linhas3 = listaPERFUMARIA.readlines()
        for linha in linhas3:
            print(green + f'{linha.strip()}' + normal)
        print('¨¨' * 38)
        print('¨¨' * 38)
        print(texto_DERMO_lista_centralizado)
        with open("listaDERMO.txt", "r") as listaDERMO:
            linhas3 = listaDERMO.readlines()
        for linha in linhas3:
            print(green + f'{linha.strip()}' + normal)
        print('¨¨' * 38)
        print('¨¨' * 38)
