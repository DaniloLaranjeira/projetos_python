palavras = ('carro', 'janela', 'computador', 'livro', 'cachorro', 'telefone', 'praia', 'montanha', 'chave', 'cadeira')

for p in palavras:
    print(f'\nNa palavra {p} temos: ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')