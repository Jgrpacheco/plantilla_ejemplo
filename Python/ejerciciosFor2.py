"""print("ejerccio para ingresar 10 nume y mostrar la suma de los 5 primeros ")

x=0
total=0
for i in range(10):
      dato=int(input("ingrese el dato : "))
      total=total+dato
      x=x+1
if x==5:
 print (total)"""


print ("ingrese el valor entero de  la tabla de multiplicar que desea")
valor=int(input("ver la tabla del ...? -> "))
 
a=0
y=0

for i in range(13):
   y=valor*i 
   print (str(valor)+" X "+str(i)+" = "+str(y))  
