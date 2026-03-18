preco = float(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTOS 
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")

resp = int(input("Informe a opção de pagamento: "))

if resp == 1:
    total = preco - (preco * 10 / 100)
elif resp == 2:
    total = preco - (preco * 5 / 100)
elif resp == 3:
    total = preco
elif resp == 4:
    total = preco + (preco * 20 / 100)
else:
    print("Opção inválida, tente novamente!")

print("Sua compra de R${:.2f} vai custar R${:.2f}".format(preco, total))