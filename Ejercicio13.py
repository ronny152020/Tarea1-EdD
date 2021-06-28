class ejercicio13:
    def __init__(self):
        pass
    
    def Buclecenti (self):
        suma=0
        producto=1
        num=int(input("Ingrese un numero: "))
        while num!=-1:
            suma=suma+num
            producto=producto*num
            num=int(input("ingrese otro numero: "))
        print("El total de la suma es de: ",suma)
        print("El total del producto es de: ",producto)

centinela=ejercicio13()
centinela.Buclecenti()