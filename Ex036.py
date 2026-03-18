val = int(input("Qual o valor da casa?"))
sal = int(input("Qual o seu salário?"))
tempo = int(input("Em quantos anos você vai pagar a casa?"))

prest = val / (tempo * 12)

if prest > (sal / 10) * 3:
   print ("O empréstimo não foi autorizado.")
else:
   print ("O empréstimo foi concedido com sucesso!")