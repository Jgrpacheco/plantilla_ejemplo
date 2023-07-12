#print("Hello World")#
print("ingrese 4 valores , se mostrara la suma de los dos primeros y el producto de los siguientes")
a=int(input("ingrese el primer numero:"))
b=int(input("ingrese el segundo numero:"))
c=int(input("ingrese el tercero numero:"))
d=int(input("ingrese el cuarto numero:"))

suma=a+b
producto=c*d
total=a+b+c+d
promd=total/4
porcentaje=suma*100//total

print("la suma de los primeros 2 valores ingresados es:")
print (suma)
print("el producto de los siguientes es:")
print (producto)
print("la suma total es:")
print (total)
print("el promedio es:")
print (promd)
print("el porcentaje que representa la suma es:")
print (str(porcentaje)+" %")

