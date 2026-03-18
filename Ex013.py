salário = float(input('Insira seu salário: '))
aumento = salário + (salário * 15 / 100)

print('O seu antigo salário era de R${:.2f}, agora com seu aumento de 15%¨ ira para R${:.2f}.'.format(salário, aumento))