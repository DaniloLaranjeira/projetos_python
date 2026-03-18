primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))

termo = primeiro
count = 1

while count <= 10:
    print("{}".format(termo),end=" ")
    print(" --> " if count <= 10 else ".", end=" ")
    termo += razão
    count += 1
print("FIM!")