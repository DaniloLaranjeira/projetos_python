soma = 0
for n in range (3, 501, 3):
    if n % 3 == 0: soma = soma + n
    
print("A soma de todos os valores é {}".format(soma))