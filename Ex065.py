soma = count = maior = menor = 0
resp = "S"

while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    count +=1
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N]")).upper().strip()

print("Você digitou {} e a média deles é {}".format(count, soma / count))
print("O maior valor foi: {}".format(maior))
print("O menor valor foi: {}".format(menor))
