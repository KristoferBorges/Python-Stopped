nomeCompleto = str(input('Seu Nome Completo: ')).strip()

print('Seu nome tem {} Letras'.format(len(nomeCompleto)))

print('Seu nome maiúsculo fica: {}'.format(nomeCompleto.upper()))

print('Seu nome minusculo fica: {}'.format(nomeCompleto.lower()))

nomeSemEspaco = nomeCompleto.replace(" ", "")
print('A quantidade de letras (Sem espaços) é de :{}'.format(len(nomeSemEspaco) - nomeCompleto.count(" ")))


separacao = nomeCompleto.split()
primeiroNome = separacao[0]
print('Seu primeiro nome é: {}'.format(primeiroNome))



