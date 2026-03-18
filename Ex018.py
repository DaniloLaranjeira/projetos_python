import math
ângulo = float(input('Informe o ângulo: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))

# O "MATH.RADIASN" CONVERTE O ÂNGULO PARA RADIANOS E APÓS ISTO CALCULA SEU SENO.