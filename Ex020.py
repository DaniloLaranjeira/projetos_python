import random
primeiro = str(input('Informe o nome do aluno: '))
segundo = str(input('Informe o nome do aluno: '))
terceiro = str(input('Informe o nome do aluno: '))
quarto = str(input('Informe o nome do aluno: '))

lista = [primeiro, segundo, terceiro, quarto]

random.shuffle(lista)

print('A ordem escolhida foi')
print(lista)

#podemos utilizar também o "from random import shuffle" e "shuffle(lista)"