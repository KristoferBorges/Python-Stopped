"""Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
import sys

print('-=' * 10, 'SORTEIO - MEGA SENA', '-=' * 10)
amount_of_games = int(input('Quantos jogos deseja sortear: '))
list_of_game = list()
games = list()
total = 1
while total <= amount_of_games:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in list_of_game:
            list_of_game.append(num)
            cont += 1
        if cont >= 6:
            break
    list_of_game.sort()
    games.append(list_of_game[:])
    list_of_game.clear()
    total += 1
sys.stdout = open('output.txt', 'w')
for i, l in enumerate(games):
    print(f'Jogo {i+1} - {l}')





