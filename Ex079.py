números = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in números:
        números.append(n)
    else:
        print("Valor duplucado. Não vou adicionar...")
    resp = str(input("Quer continuar? [S/N]")).upper().strip()
    if resp in "Nn":
        break

números.sort()
print(f"Você digitou os valores {números}")