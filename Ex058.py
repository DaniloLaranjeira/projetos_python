from random import randint
pc = randint(0, 10)
print("Vou pensar em um número de 0 a 10. Tente adivinhar")

acertou = False
palpite = 0

while not acertou:
    jogador = int(input("Qual seu palpite? "))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print("Mais...")
        else:
            print("Menos...")

print("Acertou com {} palpites".format(palpite))