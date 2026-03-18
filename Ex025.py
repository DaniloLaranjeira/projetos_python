n = str(input("Qual seu nome completo?")).strip()

nome = n.title()
print("Seu nome tem Silva? {}".format("Silva" in nome))
