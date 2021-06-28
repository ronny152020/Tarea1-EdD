class ejercicio18:
    def __init__(self):
        pass
    
    def promedios(self):
        notas_lista=[]
        alumnos_lista=[]
        ALUMNOS=30
        CASILLAS_NOTAS=6
        promedio_examenes=[]
        for alumno in range(1,31):
            alum_temporal=input("Nombre de alumno {}: ".format(alumno))
            alumnos_lista.append(alum_temporal)
            for nota in range(1,7):
                print("escriba la calificacion del alumno {} en el examen {}".format(alum_temporal,nota))
                notas_temporal=round(float(input("nota #{}: ".format(nota))), 2)
                if nota ==1:
                    notas_lista.append([notas_temporal])
                else:
                    notas_lista[alumno-1].append(notas_temporal)
            print(" ")
        
        for numero_examen in range(6):
            suma_notas=0
            for nota in notas_lista:
                suma_notas+=nota[numero_examen]
            promedio=round((suma_notas/ALUMNOS), 2)
            print("promedio de examen {} : {} ".format(numero_examen+1,promedio))
            
        print(" ")
        for numero, alumno in enumerate(alumnos_lista):
            suma_notas=sum(notas_lista[numero])
            promedio=round((suma_notas/CASILLAS_NOTAS), 2)
            print("{} su promedio es: {} ".format(alumno, promedio))
            
        prom_mayor=0
        for numero_examen in range(6):
            suma_notas=0
            for nota in notas_lista:
                suma_notas+=nota[numero_examen]
            promedio=round((suma_notas/ALUMNOS), 2)
            if prom_mayor<promedio:
                prom_mayor=promedio
            promedio_examenes.append(promedio)
        print(" ")
        print("El examen",promedio_examenes.index(prom_mayor)+1,"obtuvo el mayor promedio: ",prom_mayor)
        
arreglo=ejercicio18()
arreglo.promedios()

         