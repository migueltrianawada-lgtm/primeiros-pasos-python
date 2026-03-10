
# 1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior. #

n1 = int(input('escreva um  numero  '))
n2 = int(input('escreva um numero  '))

if n1 > n2:
 print(f'{n1} e maior ')
elif n1 < n2:
 print(f'{n2} e maior')
else:
 print(f'{n1} e {n2} são iguais')

 
# 2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa). #

 pc = float (input('escreva o porcentual de crecimento '))
 
 if pc >= 50.0:
  print(f'{pc} o porcentagem e positivo ')
 else:
  print(f'{pc} o porcentagem e negativo ') 

# Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante. #

letra = input(' digite uma letra ')
vogal = 'a,e,i,o,u,A,E,I,O,U'
if letra in vogal:
 print(f'{letra} e uma vogal ')
else:
 print(f'{letra} e uma consoante')



# Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.#

ano1 = float(input(' valor do primeiro ano e '))
ano2 = float(input(' valor do segundo ano e '))
ano3 = float(input(' valor do treceiro ano e '))

if ano1 > ano2 > ano3:
 print(f'{ano1} e o  ano com valor mais alto e {ano3}  e o ano com valor mais baixo') 
elif ano2> ano1 > ano3:
 print(f'{ano2} e o  ano com valor mais alto e {ano3}  e o ano com valor mais baixo')
elif ano3> ano2 > ano1:
 print(f'{ano3} e o  ano com valor mais alto e {ano1} e o ano com valor mais baixo')
elif ano1> ano3 > ano2:
 print(f'{ano1} e o  ano com valor mais alto e {ano2}  e o ano com valor mais baixo')
elif ano2> ano3 > ano1:
 print(f'{ano2} e o  ano com valor mais alto e {ano1} e o ano com valor mais baixo')
elif ano3> ano1 > ano2:
 print(f'{ano3} e o  ano com valor mais alto e {ano2} e o ano com valor mais baixo ')

 


#5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.#
preço1 = float(input(' escreva o valor do produto 1 '))
preço2 = float(input(' escreva o valor do produto 2 '))
preço3 = float(input(' escreva o valor do produto 3 '))

if preço1 < preço2 < preço3:
 print(f'{preço1} e o produto 1 o mais barato')
elif preço1 < preço3 < preço2:
 print(f'{preço1} e o produto 1 o mais barato')
elif preço2 < preço1 < preço3:
 print(f'{preço2} e o produto 2 o  mais barato')
elif preço2 < preço3 < preço1:
 print(f'{preço2} e o produto 2 o mais barato')
elif preço3 < preço2 < preço1:
 print(f'{preço3} e o produto 3 o mais barato')
elif  preço3 < preço1 < preço2:
 print(f'{preço3} e o produto 3 o mais barato')

#6) Escreva um programa que leia três números e os exiba em ordem crescente.
nu1 = int(input(' escreva o primeiro  numero '))
nu2 = int(input(' escreva o segundo  numero '))
nu3 = int(input(' escreva o treceiro  numero '))
if nu1 > nu2 > nu3:
 print( f' os numero em forma crescente são {nu3},{nu2},{nu1}')
elif nu1 > nu3 > nu2:
 print( f' os numero em forma crescente são {nu2},{nu3},{nu1}')
elif nu2 > nu1 > nu3:
 print( f' os numero em forma crescente são {nu3},{nu1},{nu2}')
elif nu2 > nu3 > nu1:
 print( f' os numero em forma crescente são {nu1},{nu3},{nu2}')
elif nu3 > nu2 > nu1:
 print( f' os numero em forma crescente são {nu1},{nu2},{nu3}')
elif nu3 > nu1 > nu2:
 print( f' os numero em forma crescente são {nu2},{nu1},{nu3}')


# 7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.#

turno = input(' escreva o turno que você estuda ')
if turno == 'manha':
 print(f'Bom Dia !')
elif turno == 'tarde':
 print(f'Boa tarde!')
elif turno == 'noite':
 print(f'Boa Noite!')
else:
 print(f'Valor Inválido!')

#Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo





# Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
# Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
# Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes.

#Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

#O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
#O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.