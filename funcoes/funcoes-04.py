# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import  sleep

def maior(*n):
    cont = maior = 0
    print('Analisando os valores...')
    for i in n:
        print(f'{i}',end=' ')
        sleep(0.5)
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont += 1
    print()
    print(f'Foram informados {cont} valores ao todo.')
    if cont == 0:
        print('Nenhum valor foi informado.')
    else:
        print(f'O maior valor informado foi {maior}')


numeros = []
while True:
    n = (int(input('Digite um número (0 para terminar): ')))
    if n == 0:
        break
    numeros.append(n)
maior(*numeros)
