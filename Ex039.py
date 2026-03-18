ano = int(input("Informe o ano em que você nasceu: "))
idade = 2025 - ano
if 2025 - ano <= 16:
    print("Ainda é cedo para se alistar! faltam {} anos".format(18 - idade))
elif 2025 - ano > 18:
    print("Passou o tempo de se alistar!!! você deveria ter se alistado há {} anos".format(idade - 18))
else:
    print("É hora de se alistar!")

#from datetime import date
#data = date.today().year
# este trecho de código importa a data dia atual