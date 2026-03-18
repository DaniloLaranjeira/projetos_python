count = tot = soma = 0

tot = int(input("Digite qualquer número [999 para parar]"))

while tot != 999:
    soma += tot
    count += 1
    tot = int(input("Digite qualquer número [999 para parar]"))
print("Você digitou {} números e a soma entre eles foi {}!".format(count, soma))