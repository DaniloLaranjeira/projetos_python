from random import randint

itens = ("pedra", "papel", "tesoura")
computador = randint(0, 2)

print("""Suas opções
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura""")

player = int(input("Qual sua jogada? "))

print("Computador jogou {}".format(itens[computador]))
print("Player jogou {}".format(itens[player]))

if computador == 0:
    if player == 0:
        print("EMPATE")

    elif player == 1:
        print("JOGADOR GANHOU")

    else:
        print("COMPUTADOR GANHOU")


elif computador == 1:
    if player == 0:
        print("COMPUTADOR GANHOU")

    elif player == 1:
        print("EMPATE")

    else:
        print("JOGADOR GANHOU")

elif computador == 2:
    if player == 0:
        print("JOGADOR GANHOU")

    elif player == 1:
        print("COMPUTADOR GANHOU")

    else:
        print("EMPATE")