#Essa atividade e uma introdução python cap 3
#          Uma introdução formal ao python

#meu primeiro hello word :) 20/05/2020 espero me orgulhar disso no futuro (estou no notebook ruim)
print ('hello word')
print('i hope enjoy phyton :)')

#basico numeros
print(2+2*(5*2))
print(5**2) #potencia
print(17/3) #divisao normal retorna o valor FLOAT
print(17//3) #divisao normal que descarta as virgulas INT
print(17%3) #resto da divisão, da pra verificar se o numero e par igual PHP

#variavies numericas
width = 20
height = 5*9
total= width*height
print(total)

#strings
print('minha primeira string simples')
print('my frist string, dosen\'t do that') #\ serve pra vc colocar aspas dentro da aspas (ou)
print("dosen't") #ou
print('"Yes" they said')
print('"Isnt\'t", they said')

#/n quebra de linha
print('Oi tudo bem?\nCom voce?')
#r antes da 1 aspas
print('C:\some\name')
print(r'C:\some\name')

#""" escreve tudo completo
print("""
  meu 
  deus
  do
  ceu
  """)

#concatenacao de strings
#3x 'oi', seguido de um tudo bem
print(3*'oi'+'tudo bem?')

#quebrando string longa
print('Oi tudo bem? essa string e grande e uma string'
      'na frente da outra, elas se juntam em uma so,'
      'como se fosse uma frase.\n')

#concatenar variavel
prefixo = 'Py'
completo = prefixo + 'thon'
print(completo)

#indexando strings
#caso eu coloque - ira pegar em ordem decrescente
word = 'python'
print(word[0]) #carctere posicao 0
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
print(word[-1]) #ultimo caractere
print(word[-2]) #second - last
print(word[-3])
print(word[-4])
print(word[-5])
print(word[-6])
print('\n')

#slicing  fatiamento
print(word[0:2]) #caracteres da posicao 0 ate a 2
print(word[2:6]) #caracteres da posicao 2 ate a 6
print('\n')

#substring
# 0 1 2 3 4 5 6
# p y t h o n|

print(word[0:2]) #caracteres da posicao 0(incluso) para 2(excluso)
print(word[2:5]) #caracteres da posicao 2(incluso) para 5(excluso)
print(word[:2] + word[2:]) #Inicio sempre incluido e o fim sempre excluido garente quem iguais
print('\n')
#o primeiro indice omitido e por padrao 0, e o segundo por padrao e o tamanho da string
#sendo fatiada

#funcao len()
#serve para retornar o tamanho de uma string
print(len(word))
print('\n')

#LISTAS
#insere valores diversos por ,

lista = [1,4,9,16,25]
print(lista)
print('\n')

#a lista pode ser indexada e fatiada
print(lista[0])
print(lista[-1])
print(lista[-3:])
print(lista[:]) #copia da lista
print(lista+[11,22,33,44,55,66,77,88,99])#concatenacao com a lista
print('\n')

#Diferentes das strings que sao imutaveis, a lista vc pode alterar determinados
#elementos de dentro deleas

lista2 = [1,8,27,65,125] #tem coisa errada,vou mudar
print(lista2) #lista sem nenhum valor alterado
print(4 ** 3) #o cubo de 4 e 64, nao 65
lista2[3] = 64 #recolocando um valor, pelo valor correto
print(lista2) # lista com valor alterado
print('\n')

#metodos append(), sereve para adicionar valor ao final da lista

lista2.append(216) #adiciona 216 ao final da lista
print(lista2)
lista2.append(7**3) #adiciona o cubo de 7 no final da lista
print(lista2)
print('\n')
#atribuicao de fatia te permite alterar o tamanho da lista ou remover tudo

lista3 = ['a','b','c','d','e','f','g']
print(lista3)
#realocando valores
lista3[2:5] = ['C','D','E']
print(lista3)
#removendo valores
lista3[2:5] = []
print(lista3)
#limpando a lista por completo
lista3[:] = []
print(lista3)
#a funcao len() tambem se aplica a lista
tamanho = len(lista3)
print(tamanho)
print('\n')

#criando listas contendo outras listas

a = ['a','b','c'] #uma lista
n = [1,2,3] #outra lista
x = [a,n] # uma lista contendo 2 listas diferentes
print(x) #lista X no console
print(x[0]) #posicao 0 da lista x
print(x[0][1]) #posicao 0 da lista e posicao do item 1 da lista
print('\n')

#PRIMEIROS PASSOS DA PROGRAMAÇÃO
#SEQUENCIA DE FIBONACCI
#A SOMA DOS DOIS NUMEROS DEFINEM O PROXIMO

a, b = 0, 1
cont = 0
while a < 10000:
    print('Soma:',cont,'Resultado', a, end=', ') #end transforma o jeito de saido do print para mesma linha
    a, b = b, a+b
    cont += 1










