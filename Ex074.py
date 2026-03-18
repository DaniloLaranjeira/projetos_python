from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)

print('Os números sorteados foram: ', end = ' ')
for n in num:
    print(f'{n}', end = '\n')

print(f'O maior valor sorteado foi: {max(num)}')
print(f'O menor valor sorteado foi: {min(num)}')