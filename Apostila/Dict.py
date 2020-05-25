"""Um dicionario e uma colecao de elementos onde e possivel utilizar
como indice, qualquer tipo de imutavel, como strings, tuplas e tipos
numericos.
O termo e comumente utilizado para descrever a associacao entre indice
e elemento key."""
#key/value ou chave/valor

dados = {'nome': 'Ford', 'idade': 42}
print('Nome:', dados['nome'],'Idade:', dados['idade'])

#podemos inserir valores e apagar
dados['telefone']= 31998548184
del dados['idade']

#oprações

#keys() retorna uma lista das chaves de um dicionario
dados = {'nome': 'Luiz', 'idade': 18}
print(dados.keys())

#values() retorna uma lista de valores
print(dados.values())

#items() retorna uma lista contendo valor e chaves
print(dados.items())



