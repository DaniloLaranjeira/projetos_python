from traceback import print_tb

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("Os segmentos acima PODEM formar um triângulo!!!", end="")
    if r1 == r2 == r3:
        print("Este triângulo possúi todos seus lados iguais. Logo ele é um triângulo equilátero")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Este triângulo possúi dois lados iguais. Logo ele é um triângulo isóleces")
    else:
        print("Este triângulo possui todos seus lados diferentes. Logo ele é um triângulo escaleno")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo!!!")