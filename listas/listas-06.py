# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista = []
abre = fecha = 0
expressao = str(input('Digite a expressão: '))
for i, j in enumerate(expressao):
    if j == '(':
        abre += 1
    if j == ')':
        fecha += 1
if abre == fecha:
    print('Expressão válida!')
else:
    print('Expressão inválida')
