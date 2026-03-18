from random import randint
from time import sleep

itens = ("pedra", "papel", "tesoura")
computador = randint(0, 2)

print("""Suas opções:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura""")

try:
    player = int(input("Qual sua jogada? "))
    if player not in [0, 1, 2]:
        print("Jogada inválida!")
    else:
        print("JO")
        sleep(0.5)
        print("KEN")
        sleep(0.5)
        print("PÔ!\n")
        sleep(0.5)

        print(f"Computador jogou: {itens[computador]}")
        print(f"Jogador jogou: {itens[player]}")

        if computador == player:
            print("EMPATE")
        elif (computador == 0 and player == 1) or \
             (computador == 1 and player == 2) or \
             (computador == 2 and player == 0):
            print("JOGADOR GANHOU")
        else:
            print("COMPUTADOR GANHOU")

except ValueError:
    print("Por favor, digite apenas números (0, 1 ou 2).")
