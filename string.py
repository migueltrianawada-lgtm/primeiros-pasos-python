curso = " Python "
print(curso.upper())

print(curso.lower())

print(curso.title())

print(curso.strip())

print(curso.lstrip())

print(curso.rsplit())

print(curso.center(18,"#"))

print(".".join(curso))
# Old style %
nome = "Miguel"
idade = 38
profissao = "Programador"
linguagem = "Python"


print("Ola, me chamos %s. Eu tenho %d anos de idade ,trabalho como %s e estou matriculado no curso de %s." %(nome,idade,profissao,linguagem))

#metodo format

print("Ola, me chamo {}. Eu tenho {} anos de idade ,trabalho como {} e estou matriculado no curso de {}." .format(nome,idade,profissao,linguagem))

print("Ola, me chamo {3}. Eu tenho {2} anos de idade ,trabalho como {1} e estou matriculado no curso de {0}." .format(linguagem,profissao,idade,nome))

print("Ola, me chamo {nome}. Eu tenho {idade} anos de idade ,trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))




#f-string
print(f"Ola, me chamo {nome}. Eu tenho {idade} anos de idade ,trabalho como {profissao} e estou matriculado no curso de {linguagem}.")
#Formatar com  strings com f- string
PI = 3.14159

print(f" Valor de PI : {PI}")
print(f" Valor de PI : {PI: .2f}")

print(f" Valor de PI : {PI: 10.2f}")

#fatiamento

nome = "Miguel Enrique Palacios Triana"

print(nome[0])

print(nome[:9])

print(nome[10:])

print(nome[10:16])

print(nome[10:16:2])
#copia da string
print(nome[:])
#copia e espeliar 
print(nome[::-1])

#string triplas
mensagem = f"""
 ola meu nome é {nome},
 Eu estou aprendendo Python. 
  Essa mensagem tem diferentes recuos
   """

print(mensagem)

print("""
====Menu=====
 1 -Depositar
 2 -Sacar
 3 -Sair  
=============
   """)


