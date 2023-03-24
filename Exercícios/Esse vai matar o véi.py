nomes = ''
idades: int = 0
sexos = ''
media_idade = 0
homem_mais_velho = 0
m_menos_20 = 0

for i in range(1, 4+1):
    nomes = str(input('Seu nome ({}): '.format(i)))
    idades = int(input('Sua idade ({}): '.format(i)))
    sexos = str(input('Seu sexo M/F ({}):'.format(i))).upper()

    media_idade = media_idade + idades
    if i == 1 and sexos == 'M':
        homem_mais_velho = idades
    elif idades > homem_mais_velho:
        homem_mais_velho = nomes
    if m_menos_20 <= 20 and sexos == 'F':
        m_menos_20 = m_menos_20 + 1

print('A média das idades listadas foi de {} anos!'.format(media_idade / 4))
print('O homem mais velho listado foi o Sr.{}!'.format(homem_mais_velho))
print('Na lista tivemos {} pessoas com menos de 20 anos do sexo Feminino!'.format(m_menos_20))
