num = int(input("Digite um número: "))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        total += 1
    else:
        print("{}".format(c), end= " --> ")
print("o número {} foi divido {} vezes.".format(num, total))
if total == 2:
    print("Por isso ele é primo!")
else:
    print("Por isso ele não é primo!")