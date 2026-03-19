#1. Escreva um código que lê a lista abaixo e faça:
#A leitura do tamanho da lista
#A leitura do maior e menor valor
#A soma dos valores da lista

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

def leitura(dados):
   # 1. Leitura do tamanho da lista
   tamanho = len(dados)
   # 3. Soma dos valores da lista
   soma = sum(dados)
   # 2. Leitura do maior e menor valor
   menor = min(dados)
   maior = max(dados)

   return tamanho,soma,maior,menor

# Chamando a função e desempacotando os resultados
tamanho,soma,maior,menor = leitura(lista)

# Exibindo os resultados de forma clara
# Exibindo os resultados de forma clara
print(f"Tamanho da lista: {tamanho}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Soma dos valores: {soma}")

#como foi solicitado :

print(f"A lista possui {tamanho} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores presentes nela é igual a {soma}")


#2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:
# Solicita a entrada do usuário e converte para inteiro
numero = int(input(f'digite o numero  '))

def tabulada():
   # O range(11) vai de 0 até 10
   for elemento in  range(11):
      resultado = numero * elemento
      print(f'{numero} * {elemento} = {resultado}')


(print(f'Tabuladada do {numero}:'))
# Chamando a função para executar
tabulada()
         

