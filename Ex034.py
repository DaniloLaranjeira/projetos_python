sal = float(input("Informe seu salário: "))

if sal > 1250:
    print("Seu aumento é de 10%. Seu novo salário é de R${:.2f}".format((sal * 0.10) + sal))
else:
    print("Seu aumento é de 15%. Seu novo salário é de R${:.2f}".format((sal * 0.15) + sal))