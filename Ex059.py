from time import sleep

n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))

opção = 0

while opção != 5:
    print("""    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR""")

    opção = int(input(" ---> Qual sua opção: "))

    if opção == 1:
        soma = n1 + n2
        print("A soma de {} mais {} é {}!".format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print("O resultado de {} vezes {} é {}!".format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("Entre {} e {} o maior é {}!".format(n1, n2, maior))
    elif opção == 4:
        print("Informe os números novamente:")
        n1 = int(input("Informe o primeiro valor: "))
        n2 = int(input("Informe o segundo valor: "))
    elif opção == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente")
    sleep(1.2)
print("Fim do programa. Volte sempre!")