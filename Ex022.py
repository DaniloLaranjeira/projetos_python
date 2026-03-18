Nome = str(input('Digite seu nome completo: ')).strip()
M = Nome.upper()
m = Nome.lower()
l = len(Nome)-Nome.count(' ')
f = Nome.find(' ')
p = Nome.split()

print('Analisando seu nome...')

print("""Seu nome em maiúsculo é {} 
Seu nome em minúsculo é {}
Seu nome tem {} letras
Seu primeiro nome é {} e tem {} letras""".format(M, m, l, p[0], f) )