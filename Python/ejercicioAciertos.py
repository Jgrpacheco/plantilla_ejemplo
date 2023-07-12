"""Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
	Nivel máximo:	Porcentaje>=90%.
	Nivel medio:	Porcentaje>=75% y <90%.
	Nivel regular:	Porcentaje>=50% y <75%.
	Fuera de nivel:	Porcentaje<50%."""

print ("Bienvenidos este programa muestra el porcentaje de aciertos.")
print ("Ingrese cantidad de preguntas y luego num de aciertos.")

a=int(input("ingrese num de preguntas realizadas: "))
b=int(input("ingrese num de respuestas correctas: "))

porcentaje=(b*100)//a

if b>a:
  print("ERROR !!! el num de aciertos no puede ser mayor a las preguntas realizadas.")
else:  
 print("El nivel obtenido segun sus respuestas es: ")
 if porcentaje>=90:
     print("Nivel máximo: con un "+str(porcentaje)+ "%  de aciertos")
 else :
    if porcentaje<90 and porcentaje>=75:
     print("Nivel medio: con un "+str(porcentaje)+ "%  de aciertos")
    else:
     if porcentaje < 75 and porcentaje >=50:     
      print("Nivel regular: con un "+str(porcentaje)+ "%  de aciertos")
     else:  
      print("Fuera de Nivel: con un "+str(porcentaje)+ "%  de aciertos")