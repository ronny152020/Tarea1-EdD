class ejercicio4:
    def __init__(self):
        pass
    
    def paseaño (self):
        nota=0
        nota=float(input("Ingrese su calificacion: "))
        if nota>=7:
            print("Usted esta aprobado")
        else:
            print("Usted ha reprobado, disculpa ")
            
examen=ejercicio4()
examen.paseaño()