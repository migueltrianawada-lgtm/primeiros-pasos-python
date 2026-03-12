#1) Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses valores, faça um programa que calcule a média de gastos. Dica: use as funções built-in sum() e len()

lista1 = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

suma = sum(lista1)
quantidade = len(lista1)
media = suma / quantidade
print(f'A media de gastos da empresa de papel e {media} Reais')

# Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

conteo =0
compras = len(lista1)
for valor in lista1:# o valor percorre e recebe o valor da lista 
    if valor > 3000:
        conteo += 1
        
    porcetagem = (conteo/compras)*100

print(f'quantidade de compras realizadas foram {conteo}')
print(f'o porcentagem total das comprar {porcetagem:.1f}%')

#3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].    
             
lista2 =[]

for i in range (5):
    item = int(input(f'Digite os  numero inteiros  '))
    lista2.append(item)#adicinando o valor input

    print(f'a lista que digito foi {lista2}')

    #4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

lista3 = []
for i in range(6):
    items = int(input('digite  numero inteiros  '))
    lista3.append(items)

    print(f' a lista digitada impimida de manera inversa e {lista3[::-1]}')#imprime alista de manera inversa

#5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.



#6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.


#7) Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).

#8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.

#9) Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.
#Gabarito da prova:
###01 - D
#02 - A
#03 - C
#04 - B
#05 - A
#06 - D
#07 - C
#08 - C
#09 - A
#10 - B
#10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).

#11) Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário: