class ejercicio2:
    def __init__(self):
        pass
    
    def comisiones (self):
        sueldob, ven1, ven2, ven3, porcomi= 0,0,0,0,0.10
        sueldob=int(input("Ingrese su sueldo: "))
        ven1=int(input("Ingrese su primera vente: "))
        ven2=int(input("Ingrese su segunda vente: "))
        ven3=int(input("Ingrese su tercera venta: "))
        totalven=ven1+ven2+ven3
        comision=totalven*porcomi
        Totalsueldo= sueldob+comision
        print("Su comision de este mes es de :",comision)
        print("Su total de sueldo con comisiones es de: ",Totalsueldo)
        
sueldo=ejercicio2()
sueldo.comisiones()
        