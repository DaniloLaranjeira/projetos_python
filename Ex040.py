n1 = float(input("Informe sua primeira nota: "))
n2 = float(input("Informe sua segunda nota: "))
m = (n1 + n2) / 2

if m < 5:
    print("Sua média foi de {}. Você foi reprovado!!!".format(m))
elif m < 6.9:
    print("Sua média foi de {}. Você está de recuperação!!!".format(m))
else:
    print("Sua média foi de {}. Parabéns, você foi aprovado!!!".format(m))