# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

jogo = [0, 0, 0, 0, 0, 0]
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'Sorteando {jogos} jogos')
for i in range(0, jogos):
    sleep(1)
    for j in range(0, 6):
        jogo[j] = randint(1, 60)
    print(f'Jogo {i + 1}: {jogo}')
