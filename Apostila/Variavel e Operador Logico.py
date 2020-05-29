# apostila pagina 32
# Determinando tipo variavel

#a funcao type retorna qual o tipo da variavel
b='python'
c=[2,2,3,4]
d = {'a': 1, 'b': 2}
print(type(d))
print(type(b))
print(type(c))

#a funcao len retorna o tamanho da variavel dependendo do seu tipo

print(len(b))
print(len(c))
print(len(d))

#len e type representam funcoes de retrospeccao
#Conversao de variaveis

a = '1'       #type = string
b = int(a)    #type = int
print(type(b))
c = 1         #type = int
d = float(c)  #type = float
print(type(c))
e = [1,2,3,4] #type = list
f = tuple(e) #type = tuple
print(type(f))
g = 'False' #type string
h = bool(g) #trype bool
print(type(h))

#avaliacao true ou false
#todos valores avaliados como false
''''
    False
    none
    Qualquer numero com zero(0,0L,0.0, 0j)
    Qualquer sequencia vazia '',(),[]
    Qualquer dicionario vazio {}
'''

#operadores

"""
+ 
-
*
/
// divisao truncada (parte inteira)
% resto divisao
** expodenciacao
"""

print(21.34321//2) #retorna 10 ao invez de 10.676721
print(10%2) #retorna 0, que e o resto invez de 5

#outro metodo de expodenciacao (parece com C)
print(pow(3,2))

#a funcao math da biblioteca padrao possui funcoes ja prontas
#para calculos como fatorial,seno coseno,logaritimo, raz...

'''
Operadores de atribuicao
+= soma  e atribui
-= subtrai e atribui
*= multiplica e atribui
/= divide atruibui
//= ...
%= ..
**= .. 
'''

#operadores podem ser utilizados em strings,listas,e tuplas
a = [-1,-2]
b=[1,2,3]
print('b*3' , b*3)
print('a+b', a+b)
c = (1,2)
print('c+(3,4)',c+(3,4))

#operadores logicos

"""
>
<
>=
<=
==
not Não e
!=  Diferente ou igual
and E
or  OU
"""

print(not 5<3) #TRUE


