# Material de controle de Fluxo
#Capitulo 4

#Comandos if

x = int(input("Please enter a integger value: \n"))
print('Input value: ',x)
if x < 0:
    x = 0
    print('Negative value change to zero.\n'
          'New value: ',x)
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


#Comando for

words = ['cat','widow','nukebomb']
for n in words:
    print(n,len(n))

