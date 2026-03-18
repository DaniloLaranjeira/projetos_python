from random import randint
pc = randint(0, 5)
print("Vou pensar em um número de 0 a 5. Tente adivinhar")
player = int(input("Em que número eu pensei? "))

if player == pc:
    print("PARABÉNS! Você venceu!")
else:
    print("GANHEI! Eu pensei no número {}".format(pc))