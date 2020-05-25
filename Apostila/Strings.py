#String pagina 24
x = 'Teste, '
print(x , 'Testado')
print('Python e: ' + 'bom dimais')

#slice de strings

string = 'Python'
print(string[0])
print(string[1:3])
print(string[3:])
print(string[:9])

#formatacao de strings
#metodo format
#consiste em placeholders por posicoes ou palavras chaves

string1 = "{0}+{1}={2}" #Por index
print(string1.format(1,1,2))

string2 = 'Nome: {nome}, Idade: {idade}' #Por chave
print(string2.format(nome='Lhuizito', idade='18'))

print( """\n{saudacao}!
Agora sao exatamente {hora:02d}:{minuto:02d}""".format(saudacao='Bom dia',hora=3,minuto=5))
#d um simbulo de formatacao pra ficar num formato que aceita nº base 10
#tem varios outros formatos 02 e para ficar 2 casas


#Operacoes string

#captalize() copia e retorna o valor da string com a 1 letra maiuscula
string = 'python'
print('Captalize: ',string.capitalize()) #era minusculo

#upper() retorna TODA string com letra maiuscula
print('Upper: ',string.upper())#era tudo minusculo

#lower() retorna toda string em minusculo
string = 'PYTHON'
print('Lower: ', string.lower())#era tudo maiusculo

#strip() retorna uma copia da string com os valores em branco removidos
string = '          python              '
print('Padrao: ',string)
print('Strip: ',string.strip())

#startwith() retorna true ou false se a string comecar com o prefixo
string = 'python'
print('StartWith False:',string.startswith('PY'))
print('StartWith True:',string.startswith('pyth'))

#metodos como captalize(deixa maisculo) e lower(deixa minusculo)
#como as strings sao imutaveis, eles nao fazem modificacoes nelas
#eles fazem apenas copias
#para mudar as strings vc precisa

string = "PYTHON"
string = string.lower()
print('Valor MUDADO,NÃO COPIADO: ', string)
