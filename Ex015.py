Carro = int(input('Quantos dias o carro foi alugado: '))
KM = float(input('Quantos quilômetros foi percorrido com o carro: '))
valor = (Carro * 60) + (KM * 0.15)

print('O total a pagar é R${:.2f}'.format(valor))