# Recebendo as notas e calculando a média ponderável
N1 = float(input("Digite a 1ª nota do(a) estudante: "))
N2 = float(input("Digite a 2ª nota do(a) estudante: "))
N3 = float(input("Digite a 3ª nota do(a) estudante: "))

media_ponderavel = lambda x,y,z: (x*3 + y*2 + z*5) / 10
media_estudante = media_ponderavel(N1,N2,N3)
print(f'A média ponderada do(a) estudante é {media_estudante}')
#Recebemos mais uma demanda, desta vez, para criar uma pequena função que pudesse adicionar qualitativo (pontuação extra) às notas do trimestre dos estudantes da turma que ganhou a gincana de programação promovida pela escola. Cada estudante receberá o qualitativo de 0.5 acrescido à média.

#Os dados recebidos correspondem a uma lista contendo as notas de alguns estudantes e uma variável com o qualitativo recebido.

notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5

notas_atulizadas = list(map(lambda x : x + qualitativo,notas))
print(f'as notas mais o quanlitativo  são  {notas_atulizadas}')

""" 
notas_atulizadas = map(lambda x : x + qualitativo,notas)
notas_atulizadas = list(notas_atulizadas)
print(notas_atulizadas)   """