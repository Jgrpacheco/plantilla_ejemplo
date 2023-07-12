"""print("Ingrese 3 notas (entre 0 y 10) del estudiante para calcular su promedio")
a=int(input("ingrese la primera nota:"))
b=int(input("ingrese la segunao nota:"))
c=int(input("ingrese la tercera nota:"))

total=a+b+c
promedio=total/3

if promedio >= 7:
    print ("Promocionado , su promedio es: " + str(promedio))

else:
    print ("Reprobado , su promedio es: " + str(promedio))  """  



num=int(input("Ingrese un valor entero de 1 o 2 dígitos:"))
if num<10:
    print("Tiene un dígito")
else:
    if num>9 and num<100:
     print("Tiene dos dígitos")
    else:
     print("el valor ingresado tiene mas de 2 digitos.")


