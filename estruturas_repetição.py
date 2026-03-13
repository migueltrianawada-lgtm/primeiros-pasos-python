contador = 1
while contador <= 3:
 nota_1 = float(input('Digite a 1° nota: '))
 nota_2 = float(input('Digite a 2° nota: '))

 print(f'Média: {(nota_1+nota_2)/2}')
 contador = contador + 1
 contadores = 1
 for contadores  in range(1,4):
  nota_1 = float(input('Digite a 1° nota: '))
  nota_2 = float(input('Digite a 2° nota: '))

 print(f'Média: {(nota_1+nota_2)/2}')
 print(contadores)

 # suma normal
suma = 0
for nota in notas.values():
  suma += nota
suma
