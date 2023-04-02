import random

al1 = str(input('Primeiro Aluno: '))
al2 = str(input('Segundo Aluno: '))
al3 = str(input('Terceiro Aluno: '))
al4 = str(input('Quarto Aluno: '))


listAlunos = [al1, al2, al3, al4]
sorteado = random.choice(listAlunos)

print('O ALUNO SORTEADO FOI: {}'.format(sorteado))
