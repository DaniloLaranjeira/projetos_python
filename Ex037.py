num = int(input("Escolha um número inteiro: "))

print("""Escolha uma das bases para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal""")

opc = int(input("Sua opção: "))

if opc == 1:
    print("{} convertido para binário é igual {}".format(num, bin(num)[2:]))
elif opc == 2:
    print("{} convertido para octal é igual {}".format(num, oct(num)[2:]))
elif opc == 3:
    print("{} convertido para hexadecimal é igual {}".format(num, hex(num)[2:]))
else:
    print("opção inválida. Tente novamente!")