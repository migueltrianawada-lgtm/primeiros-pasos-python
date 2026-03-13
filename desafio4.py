#1Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

from random import choice
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

lista = choice(lista)
print(lista)

#2 Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
from random import randrange
for i in range(1):
    numero_sorteo = []
    numero_sorteo.append(randrange(100))
    print(numero_sorteo)

#3 Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

import math
base = int(input('digite a base '))
exponente = int(input('digite o exponente '))

resultado = math.pow(base,exponente)

print(f'o calculo da operação de pontecias entre {base} e {exponente} e {resultado:.2f}')

#4 Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.



for i in range(1):
    participantes = int(input('digite quantos participante  são : '))
    lista2 = []
    lista2.append(randrange(participantes))

print(f'O numero ganador do sorteo e o numero {lista2}')

  