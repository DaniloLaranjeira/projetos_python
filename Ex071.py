valor = int(input("Qual valor deseja sacar? R$"))
total = valor
cedatual = 50
totced = 0

while True:
    if total >= cedatual:
        total -= cedatual
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R${cedatual}")
        if cedatual == 50:
            cedatual = 20
        elif cedatual == 20:
            cedatual = 10
        elif cedatual == 10:
            cedatual = 1
        totced = 0

        if total == 0:
            break