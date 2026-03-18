Preço = float(input('Insira o preço do produto: '))
Desconto = Preço * 0.05
Valor = Preço - Desconto
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(Preço, Valor))

#Desconto = preço - (preço * 5 / 100)
