# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores:',end=' ')
for i in range(0,4):
    print(f'{n[i]}',end=' ')
print()
print(f'O valor 9 apareceu {n.count(9)} vezes')
par = 0
for i in range (0,4):
    if n[i] == 3:
        print(f'O valor 3 apareceu na {i+1}ª posição')
if 3 not in n:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram:',end=' ')
for i in range (0,4):
    if n[i] % 2 == 0:
        print(n[i],end=' ')
