class ejercicio14:
    def __init__(self):
        pass
    
    def numberprimo (self):
        i=1
        divisores=0
        num=int(input("Ingrese un numero: "))
        while i<=num:
            if num%i==0:
                divisores+=1
            i+=1
        if divisores==2:
            print("El numero {} es primo ".format(num))
        else:
            print("El numero {} no es primo ".format(num))
            
primo=ejercicio14()
primo.numberprimo()