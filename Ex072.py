# tupla com os números por extenso de 0 até 20
numeros = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
    'dezessete', 'dezoito', 'dezenove', 'vinte'
)

# loop para garantir que o número digitado é válido (entre 0 e 20)
while True:
    entrada = input('Digite um número entre 0 e 20: ')

    try:
        n = int(entrada)  # tenta converter a entrada para inteiro
    except ValueError:
        print('Valor inválido. Digite apenas números inteiros.')
        continue

    if 0 <= n <= 20:  # verifica se está no intervalo permitido
        break
    else:
        print('Número fora do intervalo. Tente novamente.')

# imprime somente o número por extenso, sem mostrar o número digitado
print(f'Você digitou o número {numeros[n]}')

