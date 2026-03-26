estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]

from random import randint

def gera_codigo():
  return str(randint(0,999))

codigo_estudantes = []

for i in range(len(estudantes)):
  codigo_estudantes.append((estudantes[i],estudantes[i][0]+gera_codigo()))
print(codigo_estudantes)

frutas = ("laranja","pera","uva",)

letras = tuple("python")

numeros = tuple([1,2,3,4,1])

pais = ("Brasil",)

print(frutas)
print(letras)
print(numeros)
print(pais)





