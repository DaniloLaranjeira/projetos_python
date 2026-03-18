import random
primeiro = str(input('Informe o nome do aluno: '))
segundo = str(input('Informe o nome do aluno: '))
terceiro = str(input('Informe o nome do aluno: '))
quarto = str(input('Informe o nome do aluno: '))

lista = [primeiro, segundo, terceiro, quarto]

sorteado = random.choice(lista)

print('O aluno escolhido foi {}'.format(sorteado))