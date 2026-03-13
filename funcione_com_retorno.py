
notas = [8.5, 9.0, 6.0, 10.0]

def media(lista):
  calculo = sum(lista) / len(lista)
  return calculo

resultado = media(notas)
print(resultado)

def boletim (lista):
  media = sum(lista) / len(lista)
  if media >= 6.0:
    situacao = "Aprovado(a)"
  else:
    situacao = "Reprovado(a)"
  return (media, situacao)

media_final,status = boletim(notas)

print(f' a media final e {media_final} eo status e {status}')

# a nossa função recebe uma lista do tipo list e retorna uma variável do tipo float
def medias(lista: list) -> float:
  calculo = sum(lista) / len(lista)
  return calculo


