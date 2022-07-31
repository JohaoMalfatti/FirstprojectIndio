from msilib.schema import Class

###IF
a = 12
b = 6 
if a > b:
    print("A variável maior é a "+str(a))
if a < b:
    print("A variável maior é a b"+str(b))

###else
x =1 
y=2 
if x > y:
    print("x maior que Y "+str(x))
else:
    print("x não é maior que Y "+str(y))
 
 ###elif   
r = 1
y = 2 
if r == y: 
    print ("números iguais")
elif y > r:
    print("Y Maior  que r")
elif r > y:
    print("r menor  que y")
else:
    print("números diferentes")
 
 
 ###while
wx=1
while wx < 10:
    print(wx) 
    wx = x+1
###for

lista = [1,2,3,4,5]
lista2 =["olá","mundo","!"]
lista3 = [0,"lista",9.99]
for i in lista:
    print(i)
    