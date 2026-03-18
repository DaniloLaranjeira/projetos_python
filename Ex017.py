import math
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
hipotenusa = (co ** 2 + ca ** 2) ** (1/2)

print('O valor da cateto oposto é {}, o do cateto adjacente é {} e o comprimento da hipotenusa é {:.2f}'.format(co, ca, hipotenusa))

# import math OU from math import hypot
#co = float(input('Informe o valor do cateto oposto: '))
#ca = float(input('Informe o valor do cateto adjacente: '))
#hi = math.hypot (ca, co)
#print('A hipotenusa vai medir {:.2f}'.format(hi))