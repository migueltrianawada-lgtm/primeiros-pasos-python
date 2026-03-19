notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]
nomes = []
notas_juntas = []
#for percorrer com o metodo range  todas as notas da lista com o metodo len
for i in range(len(notas_turma)):
    # sim o i e multiplo de 4 :
    if i % 4 == 0 :
        #adicione na lista nomes o valor de i
        nomes.append(notas_turma[i])
    else:
        #caso contarios na lista notas_juntas adicione o i
        notas_juntas.append(notas_turma[i])    

        # Exibindo os resultados para conferir
print(f"Nomes: {nomes}")
print(f"Notas: {notas_juntas}")

notas = []
#for precorrer com o metodo range  todas as notas da lista de tres em tres  com o metodo len (colocamos tres paremetros pega 3 notas e pula para pegar mais tres)
for i in range(0,len(notas_juntas),3):
    #adicionado na lista otras lista = lista de listas
    notas.append([notas_juntas[i],notas_juntas[i+1],notas_juntas[i+2]])

# Exibindo os resultados para conferir
print(f"Notas: {notas}")
# Exibindo os resultados para conferir uma nota espacifica da lista de lista
print(f"Notas: {notas[0][2]}")

