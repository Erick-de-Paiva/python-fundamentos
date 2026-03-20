# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler
# a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []
totalGols = 0
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas o {jogador['nome']} jogou? '))
for i in range(0,jogador['partidas']):
    gol = int(input(f'  Quantos gols na partida {i+1}? '))
    gols.append(gol)
    totalGols += gol
print(f'O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.')
for i in range(0,jogador['partidas']):
    print(f'  Na partida {i+1}, fez {gols[i]} gols.')
print(f'Foi um total de {totalGols} gols.')
