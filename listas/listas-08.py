# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

n = [[], []]
valor = 0
for i in range(0,7):
    valor = int(input(f'Digite o {i+1}o valor: '))
    if valor % 2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
n[0].sort()
print('Os valores pares digitados foram: ',end='')
for i in n[0]:
    print(i,end=' ')
print()
n[1].sort()
print('Os valores ímpares digitados foram: ',end='')
for i in n[1]:
    print(i,end=' ')
