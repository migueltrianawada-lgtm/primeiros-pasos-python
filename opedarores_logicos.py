t1 = t2 = True
f1 = f2 = False

if t1 and t2:
  print('expressão verdadeira')
else:
  print('expressão falsa')

if f1 or f2:
 print('expressão verdadeira')
else:
  print('expressão falsa')
if not t1:
  print('expressão verdadeira')
else:
  print('expressão falsa')



  lista = 'José da Silva, Maria Oliveira, Pedro Martins, Ana Souza, Carlos Rodrigues, Juliana Santos, Bruno Gomes, Beatriz Costa, Felipe Almeida, Mariana Fernandes, João Pinto, Luísa Nascimento, Gabriel Souza, Manuela Santos, Thiago Oliveira, Sofia Ferreira, Rafael Albuquerque, Isabella Gomes, Bruno Costa, Maria Martins, Rafaela Souza, Matheus Fernandes, Luísa Almeida, Beatriz Pinto, Mariana Rodrigues, Gabriel Nascimento, João Ferreira, Maria Albuquerque, Felipe Oliveira'
print( lista)

nome_1 = 'Mariana Rodrigues'
nome_2 = 'Marcelo Nogueira'

if lista in nome_1:
  print(f'{nome_1} esta na lista')
else:
  print(f'{nome_1} não esta na lista')

if lista in nome_2:
  print(f'{nome_2} esta na lista')
else:
  print(f'{nome_2} não esta na lista')