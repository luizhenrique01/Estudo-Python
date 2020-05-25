# apostila pag 20

# Oprecoes
# Como tudo em python e objeto, temos funcoes para manipulalas

lista = [1,2,3,2]
print('lista padrao',lista)

#count retorna quantas ocorrencias especificas a lista tem
print('count: ',lista.count(2))

#index retorna o local do valor especifico
print('index: ',lista.index(2))

#append insere um objeto no final da lista
lista.append(4)
print('append: ',lista)

#insert insere no indice passado por um argumento (index"posicao"),'Elemento'
lista.insert(0,1)
print('insert: ',lista)

#remove remove a primeira ocorrencia do valor especificado
lista.remove(1)
print('remove:' ,lista)

#pop remove um elemento da lista e o retorna, o metodo aceita o arguento
#index, caso um indice nao seja especificado o ultimo elemento e removido

print('pop indexado: ',lista.pop(0)) #remove o elemento do indice 0 e o retorna
print('pop sem indeex: ',lista.pop()) #remove o elemento do final
print(lista)

"""o metodo short serve para ordenar a lista em ordem crescente
ou em ordem decrescente, o metodo aceita o paramentro reverse=true,
para ser ordem decrescente"""

lista.sort()
print('lista ordenada crescente: ',lista) #sem nenhum argumento
lista.sort(reverse=True)
print('lista ordenada decrescente: ',lista)

