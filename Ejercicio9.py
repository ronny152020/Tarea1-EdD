class ejercicio9:
    def __init__(self):
        pass
    
    def operadorand (self):
        nota1, nota2=0,0
        nota1=float(input("Ingrese la nota del primer examen: "))
        nota2=float(input("Ingrese la nota del segundo examen: "))
        if nota1>=80 and nota2>=80:
            print("Es aceptado")
        else:
            print("Usted ha sido rechazado")
    
    def operadorOR (self):
        nota1, nota2=0,0
        nota1=float(input("Ingrese la nota del primer examen: "))
        nota2=float(input("Ingrese la nota del segundo examen: "))
        if nota1>=90 or nota2>=90:
            print("Es aceptado")
        else:
            print("Usted ha sido rechazado")
            
operador1=ejercicio9()
operador1.operadorand()
operador2=ejercicio9()
operador2.operadorOR()