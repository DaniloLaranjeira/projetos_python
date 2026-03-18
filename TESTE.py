n = str(input("Digite seu nome completo: ")).strip()

name = n.capitalize() #opicional
nome = name.split()

print("Seja bem-vindo {}".format(n))
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu primeiro nome é {}".format(nome[len(nome)-1]))

print('{}'.format(n[:4]))