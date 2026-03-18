pri = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
dec = pri + (10 - 1) * razao

for c in range (pri , dec + razao, razao):
    print("{}".format(c),end=" --> ")
print("ACABOU!")