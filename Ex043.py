altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Seu imc é {}. Você está abaixo do peso!".format(imc))
elif imc < 25:
    print("Seu imc é {}. Você está com o peso ideal!".format(imc))
elif imc < 30:
    print("Seu imc é {}. Você está acima do peso!".format(imc))
elif imc < 40:
    print("Seu imc é {}. Você está obeso!".format(imc))
else:
    print("Seu imc é {}. Você está com obesidade mórbida!".format(imc))