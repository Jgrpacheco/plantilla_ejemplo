print("***ESTE PROGAMA INDICA LA SUMA Y RESTA SI EL PRIMER NUM ES MAYOR***")
print("***de lo contrario muestra la multiplicacion y division de ellos***")

x=int(input("ingrese el primer dato :"))
y=int(input("ingrese el segundo dato :"))

suma=x+y
resta=x-y
multiplicacion=x*y
division=y//x

if x>y:
    print("el primero es mayor se muestran la suma y resta :")
    print ("la suma es :" +str(suma))
    print("la resta es: " +str(resta))

else:
    print("El segundo es mayor se muestran la multiplicacion y division :")
    print("la multipicacion es :"+str(multiplicacion))
    print("la division es: " +str(division))
   

