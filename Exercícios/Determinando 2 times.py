import random


print('Definição de times (MINECRAFT ERA DO FUTURO)')
pessoas = ['Kristofer', 'Ramon', 'Maicon', 'Jean']
time1 = []
time2 = []

while len(pessoas) > 0:
    pessoa = random.choice(pessoas)
    pessoas.remove(pessoa)
    if len(time1) <= len(time2):
        time1.append(pessoa)
    else:
        time2.append(pessoa)

print(time1)
print(time2)
