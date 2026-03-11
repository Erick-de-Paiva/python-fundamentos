# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')
for i in range(0,len(palavras)):
    print(f'Na palavra {palavras[i]} temos essas vogais: ',end='')
    palavra = palavras[i]
    for j in range(0,len(palavra)):
        if palavra[j] in 'aeiouAEIOU':
            print(palavra[j],end=' ')
    print()
