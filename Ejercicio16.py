class ejercicio16:
    def __init__(self):
        pass
    
    def factorial (self):
        namber=int(input("Ingrese la cantidad de numeros "))
        for i in range(namber):
            numero=int(input("Ingrese un numero "))
            f=1
            for num in range(numero,0,-1):
                f=f*num
            
            print("El factorial del numero {} es de: {}".format(numero,f))

buanidado=ejercicio16()
buanidado.factorial()