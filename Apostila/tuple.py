# Tupla pagina 21
#Uma tupla consiste em valores separados por virgula
#Diferente das listas os valores sao imutaveis

t1 = 1,2,3,4,5
print('tupla 1 :', t1)
print('tupla indice: ',t1[0])
print('tupla split: ',t1[2:4])
print('tupla reverse: ',t1[::-1])

#tuple packing = qunando adiciono mais de um valor a tupla

tupla = 1,2
x,y = tupla
print('x: ',x)
print('y: ',y)

#tips and tricks Tupla

t = () #tupla vazia

x=1
print(type(x))
y=(1,)
print(type(y))

#A tupla possui dois metodos identicos as listas, index e count.
#o resto dos metodos modificam as tuplas, por isso nao sao utilizaveis,
#as tuplas sao imutaveis

