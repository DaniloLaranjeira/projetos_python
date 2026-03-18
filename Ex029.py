vel = int(input("Qual a velocidade atual do carro?"))
if vel <= 80:
    print("Tenha um bom dia! Dirija com segurança!")
else:
    print("MULTADO!!! Você excedeu o limete de volcidade permitido de 80km/h")
    print("Você deve pagar uma multa de {} R$".format((vel - 80) * 7))