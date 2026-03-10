# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
maior = menor = 0
for i in range(0,5):
    n = (randint(0,10))
    if i == 0:
        print('Os valores sorteados foram:', end=' ')
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    print(n,end=' ')
print('')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
