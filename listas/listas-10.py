# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = terceiraColuna = maiorSegundaLinha = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares = matriz[l][c] + pares
        if c == 2:
            terceiraColuna = matriz[l][c] + terceiraColuna
        if l == 1:
            if matriz[l][c] > maiorSegundaLinha:
                maiorSegundaLinha = matriz[l][c]
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end='')
        if c == 2:
            print()
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceiraColuna}')
print(f'O maior valor da segunda linha é {maiorSegundaLinha}')
