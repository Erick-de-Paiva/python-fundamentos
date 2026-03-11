# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
maior = menor = 0
for i in range(0,5):
    valores.append(int(input(f'Digite um valor inteiro para a posição {i+1}: ')))
    if i == 0:
        menor = valores[i]
        maior = valores[i]
    else:
        if valores[i] < menor:
            menor = valores[i]
        if valores[i] > maior:
            maior = valores[i]
print(f'O maior valor é {maior}, na(s) posição(ões) ',end='')
for i, j in enumerate(valores):
    if j == maior:
        print(f'{i+1}...',end='')
print()
print(f'O menor valor é {menor}, na(s) posição(ões) ',end='')
for i, j in enumerate(valores):
    if j == menor:
        print(f'{i+1}...',end='')
