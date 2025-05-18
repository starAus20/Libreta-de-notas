#Libreta de notas

#listas paralelas
nombres = ["Juan Martinez", "Andres Castillo", "Josue Villa"]
cedulas = ["0912345678","0933445566","0911223344"]
notas = [] #Habra listas dentro de una lista
totalP = [] #Total de primer parcial
totalS = [] #total segundo parcial
promedios = []
estados = [] #Lista de strings
recuperacion = []

totalAlumnos = len(nombres)

es1, es2, es3, es4, es5, es6 = 0, 0, 0, 0, 0, 0  #cantidad de estados de estudiantes


print("{:-^170}".format("Bienvenido"))

#Codigo registro de notas para cada estudiante

#for i in range(len(nombres)):

contador = 0
while contador <= (totalAlumnos-1):
    print("\nIngrese notas del estudiante: ", nombres[contador])
    
    print("\nIngrese notas del PRIMER PARCIAL\n")
    n1 = float(input("Ingrese Nota Proceso:\t"))        
    n2 = float(input("Ingrese Nota Examen:\t"))

    print("\nIngrese notas del SEGUNDO PARCIAL\n")
    n3 = float(input("Ingrese Nota Proceso:\t")) 
    n4 = float(input("Ingrese Nota Examen:\t"))

    # Validacion de numeros del 0 al 10
    if ((n1 <= 10) and (n1 >= 0)) and ((n2 <= 10) and (n2 >= 0)) and ((n3 <= 10) and (n3 >= 0)) and ((n4 <= 10) and (n4 >= 0)) :

        total1 = (n1*0.6)+ (n2*0.4)
        total2 = (n3*0.6) + (n4*0.4)

        #calculo del promedio
        promedio = (total1 + total2)/2

        #agregar a las listas correspondientes
        notas.append([n1,n2,n3,n4])
        totalP.append(total1)
        totalS.append(total2)
        promedios.append(promedio)

        #Validacion de estados
        if promedio < 3:
            estados.append("Sin derecho a recuperacion")
        elif promedio < 7.0:
            estados.append("Derecho a recuperacion")  
        elif promedio < 7.5:
            estados.append("Regular")  
        elif promedio < 8.5:
            estados.append("Bueno")  
        elif promedio < 9.5:
            estados.append("Muy bueno")
        elif promedio <= 10:
            estados.append("Excelente")
        
        #caso nota de recuperacion
        if (promedio >= 3) and (promedio <= 6.9):
            print("\nSu promedio fue de: ", round(promedio,2))
            print("\nDebio dar examen de Recuperacion")
            recu = float(input("\nIngrese nota de Recuperacion:\t"))
            recuperacion.append(recu)
        else:
            recuperacion.append(0.0)
        
        contador += 1
    else:
        print("\nNumero/s no valido/s, solo se permiten numeros del 0 al 10.\nIntente nuevamente.\n")


#Encabezado del formato
print()
print("{:>55} {:>11} {:>22} {:>10} {:>20} {:>48} ".format("PRIMER PARCIAL","Total","SEGUNDO PARCIAL","Total","  ","RECUPERACION"))
print()
print("  Cedula  \
   Apellido y nombre\
   Nota Proceso\
   Nota Examen\
     \
   Nota Proceso\
   Nota Examen\
     \
   Promedio promedio Total  \
   \tEstado    \
   \tNota Estimada del Examen",sep=" ", flush=True)


for j in range(len(nombres)):  #calculo examen de recuperacion definitivo y mostrar formato
    notaRecu = recuperacion[j]
    notaProme = promedios[j]
    if (notaProme >= 3) and (notaProme <= 6.9):
        notadef = (notaRecu*0.6) + (notaProme*0.4)
    else:
        notadef = 0.0


    print("{:<13} {:<23} {:<13} {:<10} {:<7} {:<14} {:<10} {:<13} {:<13} {:<25} {:>16}".format(cedulas[j], nombres[j], notas[j][0], notas[j][1], round(totalP[j], 2), notas[j][2], notas[j][3], round(totalS[j],2), round(promedios[j],2), estados[j], round(notadef,2)))


print()
print("Resumen General Calificaciones")
#resumen notas
print("{} {:>25} {:>15}".format("EQUIVALENCIA", "TOTAL", "PORCENTAJE"))

#catidad de estados de los estudaintes
for m in estados:
    if m == "Sin derecho a recuperacion":
        es6 += 1
    elif m == "Derecho a recuperacion":
        es5 += 1
    elif m == "Regular":
        es4 += 1
    elif m == "Bueno":
        es3 += 1
    elif m == "Muy bueno":
        es2 += 1
    elif m == "Excelente":
        es1 += 1


print("""Excelente {:>27} {:>13} %
Muy bueno {:>27} {:>13} %
Bueno {:>31} {:>13} %
Regular {:>29} {:>13} %
Derecho a recuperacion {:>14} {:>13} %
Sin derecho a recuperacion {:>10} {:>13} %
""".format(es1,round((es1*100)/totalAlumnos,1), es2,round((es2*100)/totalAlumnos,1), es3,round((es3*100)/totalAlumnos,1), es4,round((es4*100)/totalAlumnos,1), es5,round((es5*100)/totalAlumnos,1), es6,round((es6*100)/totalAlumnos,1)))

#calculo
totalPorce = (es1*100)/totalAlumnos + (es2*100)/totalAlumnos + (es3*100)/totalAlumnos + (es4*100)/totalAlumnos + (es5*100)/totalAlumnos + (es6*100)/totalAlumnos
totalEstados = es1 + es2 + es3 + es4 + es5 + es6

print("TOTAL {:>31} {:>13} %\n".format(totalEstados,totalPorce))

    










