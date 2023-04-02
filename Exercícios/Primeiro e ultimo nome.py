nomeCompleto = str(input('Digite seu nome: '))
separacao = nomeCompleto.split()
primeiroNome = separacao[0]
ultimoNome = separacao[-1]

print('Seu primeiro nome é: {}'.format(primeiroNome))
print('Seu último nome é: {}'.format(ultimoNome))
