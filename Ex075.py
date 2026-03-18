from Ex064 import count

num = (int(input("Digite um número: ")),
       int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")),
       int(input("Digite o último número: ")))

print(f'Os números digitados foram: {num} ', end = ' ')

print(f'O número 9 apareceu {num.count(9)} vezes', end = ' ')

if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1} posição', end = ' ')
else:
    print('O valor 3 não foi digitado em nenhuma posição', end = ' ')
    
for n in num:
    if n % 2 == 0:
        print(n, end = '')