# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final,
# coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogadas = {'jogador1': randint(1,6),
           'jogador2': randint(1,6),
           'jogador3': randint(1,6),
           'jogador4': randint(1,6)}
print('Valores sorteados:')
for i, j in jogadas.items():
    sleep(1)
    print(f'{i} tirou {j} no dado.')
print()
ranking = []
ranking = sorted(jogadas.items(), key=itemgetter(1),reverse=True)
print('  == RANKING DOS JOGADORES  ==  ')
for i, j in enumerate(ranking):
    print(f'  {i+1}º lugar: {j[0]} com {j[1]}.')
    sleep(1)
