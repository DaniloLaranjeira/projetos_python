soma = 0
count = 0

for c in range(1, 7):

    n = int(input("Digite seis números: "))

    if n % 2 == 0:
        soma = soma + n
        count = count + 1

print("Você informou {} números par(es) e a soma dele(s) são {}".format(count, soma))
