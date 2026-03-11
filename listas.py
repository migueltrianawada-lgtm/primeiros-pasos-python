lista = ['Fabricio Daniel', 9.5 , 9.0 , 8.0 , True]
lista[0],lista[1]
#metodo join
misturas = ['Tintas: vermelho, azul e amarelo',
            'Verde: mistura de azul e amarelo',
            'Laranja: mistura de vermelho e amarelo',
            'Roxo: mistura de vermelho e azul']
unificador = '. '
string_misturas = unificador.join(misturas)
print(string_misturas)
#metodo slipt
duvida = 'Quem veio antes? O ovo? Ou foi a serpente?'
lista_palavras = duvida.split('?')
print(lista_palavras)
media = (lista[1] + lista[2] + lista[3])/3
media
#metodo append
lista.append(media)
#metodo insert
raca_caes = ['Labrador Retriever',
             'Bulldog Francês',
             'Pastor Alemão',
             'Poodle']
raca_caes.insert(1, 'Golden Retriever')
print (raca_caes)

#metodo .pop

raca_caes.pop(1)
print (raca_caes)
#metodo .sort
raca_caes.sort()
print (raca_caes)

