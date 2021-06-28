class ejercicio12:
    def __init__(self):
        pass
    
    def Buclecondi (self):
        suma=0
        producto=1
        respuesta=input("¿Quiere comenzar con el proceso?")
        while respuesta!="n" and respuesta!="N":
            num=int(input("ingrese un numero: "))
            suma=suma+num
            producto=producto*num
            respuesta=input("¿Desea continuar(S/N)?")
        print("Total de la suma es de: ",suma)
        print("Total del producto es de: ",producto)

control=ejercicio12()
control.Buclecondi()