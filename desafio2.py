#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

conta = 1

for conta in range(1,5):
    nu1 = int(input(' escreva o numero '))
    nu2 = int(input(' escreva o numero '))
    print (f'primeiro numero {nu1} segundo numero {nu2}')


#2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.

colonia_a = 4
colonia_b =10
taxa_a = 0.03
taxa_b = 0.015

dias = 0

while colonia_a < colonia_b:
    colonia_a += colonia_a * taxa_a
    colonia_b += colonia_b * taxa_b
    dias += 1

    print(f"Levará {dias} dias para a colônia A ultrapassar ou igualar a colônia B.")
    print(f"População final de A: {colonia_a:.2f}")
    print(f"População final de B: {colonia_b:.2f}")

#3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.
quantidade = 0
 
for quantidade in range (0,3):
    nota = int(input(' escreva uma nota de 0 ate 5 '))
    if nota == (0,1,2,3,4,5):
        print(f' o valor da nota {nota}e valido')
    elif nota > 5:
        print(' valor no valido')
        quantidade -=1
        continue
    elif nota <-1:
        print(' valor no valido')
        quantidade -=1
        continue


