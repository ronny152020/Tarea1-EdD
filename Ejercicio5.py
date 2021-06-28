class ejercicio5:
    def __init__(self,limite=600):
        self.sueldo=limite
    
    def aumento (self):
        sueldini, porcentaje=0,0.1
        sueldini=int(input("Ingrese su sueldo inicial "))
        if sueldini<self.sueldo:
            sueldototal=(sueldini*porcentaje)+sueldini
            print("Su sueldo total es de: ",sueldototal)
        else:
            sueldototal=sueldini
            print("Su sueldo total es de: ",sueldototal)

sueldo=ejercicio5()
sueldo.aumento()