sexo = str(input("Informe seu sexo: [M/F]")).strip().upper()

while sexo not in "MmFf":
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo novamente: ")).strip().upper()

print("sexo {} registrado com sucesso".format(sexo))