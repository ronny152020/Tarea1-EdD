class ejercicio8:
    def __init__ (self):
        pass
    
    def funcion (self):
        num, v=0,0
        num=int(input("Ingrese un primer valor: "))
        v=int(input("Ingrese otro valor "))
        if num==1:
            resp=100*v
            print(resp)
        if num==2:
            resp=100^v
            print(resp)
        if num==3:
            resp=100/v
            print(resp)
        if num>3 and num<0:
            print(0)

multiple=ejercicio8()
multiple.funcion()