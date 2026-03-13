# Notas do(a) estudante
notas = {'1º Trimestre': 8.5, '2º Trimestre': 7.5, '3º Trimestre': 9}


# Usando a função embutida sum()
sumatorio = sum(notas.values())
print(sumatorio)

# Usando a função embutida len()
qtd_notas = len(notas)
print(qtd_notas)

# calculando a média
media = sumatorio / qtd_notas
print(media)

media = sumatorio / qtd_notas
media = round(media,1)
print(media)

#Funções sem parâmetros

def media ():
  calculo = sum(notas.values()) / len(notas.values())
  return round(calculo,1)

media()
#Funções com parâmetros
medias = []
def medias(nota_1,nota_2,nota_3):
  calculo = (nota_1 + nota_2 + nota_3) /3
  print(round(calculo))
  