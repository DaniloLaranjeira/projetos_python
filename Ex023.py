num = int(input("Informe um número: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))

#O operador % é o módulo, que retorna o resto da divisão.
#Quando fazemos num % 10, estamos pegando o último dígito do número, ou seja, a unidade .Isso significa: pegue o número, garanta que ele seja inteiro, e depois pegue o último dígito (unidade).
#123 % 10 = 3
