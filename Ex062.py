primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))

termo = primeiro
count = 1
tot = 0
mais = 10

while mais != 0:
    tot = tot + mais

    while count <= tot:
        print("{}".format(termo),end=" ")
        print(" --> " if count <= 10 else ".", end=" ")
        termo += razão
        count += 1
    print("PAUSA!")

    mais = int(input("Quantos termos a mais você deseja? "))
print("Progressãp finalizada com {} termos mostrados. FIM!".format(tot))