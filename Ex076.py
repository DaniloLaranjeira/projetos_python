Lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 18,
         'Caneta', 2,
         'Estojo', 14.99,
         'Mochila', 149.99,
         'Livro', 24.99)

for item in range(0, len(Lista)):
    if item % 2 == 0:
        print(f'{Lista[item]:.<30}', end='')
    else:
        print(f'R${Lista[item]:>7.2f}')