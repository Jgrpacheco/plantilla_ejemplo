print("imprimir con ciclo While")

"""n=int(input("¿hasta cual numero desea ejecutar la serie? "))
x=int(input("inserte el intervalo de la serie (por ejemplo:\n Si introdujo el 20 en la serie y en el intervalo 2 \n la serie se mostrara de 2 en 2 - 2,4,6,8,etc ) pudes ser el numero que desee : "))
i=0

while i<=n:   
     print(i)  
     i=i+x

print ("la serie se muestra de " +str(x)+" en "+str(x))"""

print ("Ingrese 3 numeros enteros ,de los cuales se mostrara la suma total y el promedio de ellos")

x=1
suma=0
while x<=3:
    valor=int(input("inserte el "+ str(x)+"° numero: "))
    suma=suma+valor
    x=x+1

promedio=suma/3

print("el valor de la suma es: " + str(suma))
print("el valor del promedio es : " + str(promedio))