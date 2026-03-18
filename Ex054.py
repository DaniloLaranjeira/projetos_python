from datetime import date
data = date.today().year

totalmaior = 0
totalmenor = 0

for c in range (1, 8):
    ano = int(input("Informe o ano do nascimento da {}º pessoa: ".format(c)))
    if data - ano > 18:
       totalmaior += 1
    else:
      totalmenor += 1

print("Ao todo tivemos {} pessoas de maior".format(totalmaior))
print("E também tivemos {} pessoas de menor".format(totalmenor))