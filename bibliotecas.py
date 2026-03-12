from random import choice
#from nome_biblioteca import metodo
estudantes =["João","Maria","Jose","Ana" ]
estudantes = choice(estudantes)#importa um elemento da lista random

print(estudantes)


#importando 2 metodos da biblioteca random
from random import randrange, sample

lista = []

for i in range(0, 20):
  lista.append(randrange(100))

sample(lista, 5)

#não precisamos usar o nome da biblioteca para chamar um método. Podemos passar apenas o nome dele. Por exemplo, se formos calcular a raiz quadrada de certo número poderíamos seguir por uma das duas formas:


import math 

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {math.sqrt(n)}")


from math import * 

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {sqrt(n)}")