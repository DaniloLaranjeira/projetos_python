dist = int(input("Qual a distância da viagem? (em km)"))
print("Você está prestes a começar uma viagem de {}km".format(dist))
if dist <= 200:
    print("O preço da viagem é de R${:.2f}".format(dist * 0.5))
else:
    print("O preço da viagem é de R${:.2f}".format(dist * 0.45))