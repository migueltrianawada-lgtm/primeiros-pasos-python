
#set = elimina o elementos repetidos
numeros = set([1,2,3,1,3,4])
frutas = set(("abacaxi","pera","morango","abacaxi"))
futebol = set(("palio","gol","celta","palio"))

print(frutas)
print(futebol)
print(numeros)

for i in numeros:
  print(i)

conjunto_a = {1,2,3,4}
conjunto_b = {2,3,4}

conjunto_a.union(conjunto_b)

print(conjunto_a.union(conjunto_b))

conjunto_a.intersection(conjunto_b)

print(conjunto_a.intersection(conjunto_b))

print(conjunto_a.symmetric_difference(conjunto_b))

print(conjunto_a.issubset(conjunto_b))

print(conjunto_b.issubset(conjunto_a))

print(conjunto_a.issuperset(conjunto_b))

print(conjunto_b.issuperset(conjunto_a))

sorteio = {1.23}

sorteio.add(25)
sorteio.add(43)
sorteio.add(50)

print(sorteio)



