dicionario = {'chave_1':1,
              'chave_2':2}
print(dicionario)

estudante = {'matricula':2000168933,
             'dia de cadastro':25,
             'mes de cadastro':10,
             'turma':'2E',}
print(estudante)
print(estudante['matricula'])
#modificando uma chave
estudante['turma'] = '2G'

print(estudante)
# adicionando uma chave
estudante['modalidade'] = 'EAD'
print(estudante)

#elimina o elemento
estudante.pop('turma')
#ver tds os elementos
estudante.items()
#ver tds as chaves
estudante.keys()
#ver tds valores das chaves
estudante.values()
#ver tds valores
estudante.get("matriculas")
#ver tds valores das chaves
for chaves in estudante.keys():
  print(estudante[chaves])
#ver tds valores das chaves
for valores in estudante.values():
  print(valores)
#ver tds chaves e valores
for chaves, valores in estudante.items():
  print(chaves,valores)


  loja = {'nomes': ['televisão', 'celular', 'notebook', 'geladeira', 'fogão'],
        'precos': [2000, 1500, 3500, 4000, 1500]}
  
  for chave, elementos in loja.items():
    print(f'Chave: {chave}\nElementos:')
  for dado in elementos:
    print(dado)

#A função sum() permite somar os elementos de uma sequência ou estrutura de dados. No exemplo a seguir, vamos somar os preços de produtos:

    precos = [100.0, 400.0, 200.0]
    soma = sum(precos)
    print(soma)
    
#A função help() é usada para acessar a documentação de funções, métodos e outros elementos do Python. Ela exibe informações em inglês sobre a funcionalidade, sintaxe e uso de um objeto específico. Para usar essa função, basta passar o elemento desejado entre parênteses. Por exemplo, vamos verificar a documentação da função print:

#help(print)

#Por fim, a função dir() é usada para exibir uma lista de atributos e métodos associados a um elemento. Por exemplo, vamos descobrir todos os atributos em métodos de uma lista:

#listass = [1,2,3]
#dir(listass)