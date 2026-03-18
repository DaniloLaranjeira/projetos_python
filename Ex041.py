from datetime import date
data = date.today().year

ano = int(input("Informe o ano que você nasceu: "))

idade = data - ano

if idade <= 9:
    print("Você tem {} anos! Logo é um atleta mirim".format(idade))
elif idade <= 14:
    print("Você tem {} anos! Logo é um atleta jovem".format(idade))
elif idade <= 19:
    print("Você tem {} anos! Logo é um atleta junior".format(idade))
elif idade <= 25:
    print("Você tem {} anos! Logo é um atleta sênior".format(idade))
else:
    print("Você tem {} anos! Logo é um atleta mastes!!!".format(idade))