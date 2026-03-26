nome  = input('escreva seu nome:  ')
print(nome)
ano_entrada = int(input('Escreva o ano de ingresso do(a) estudante: '))
print(ano_entrada,type(ano_entrada))

nota_entrada = float(input('Digite a nota do teste de ingresso: '))
print(f'Ano de entrada {ano_entrada} - nota do teste de ingreso {nota_entrada}')

# Leitura da entrada e conversão para inteiros
entrada = input('Escriva os numeros interos  ').split()
abertura = int(entrada[0])
fechamento = int(entrada[1])

# Comparação dos valores
if fechamento > abertura:
    print("ALTA")
elif fechamento < abertura:
    print("BAIXA")
else:
    print("ESTAVEL")

# Leitura da string de entrada
nome_destinatario = input()

# Conversão para maiúsculas
nome_maiusculo = nome_destinatario.upper()

# Exibição do resultado
print(nome_maiusculo)