class ejercicio17:
    def __init__(self):
        pass
    
    def vector(self):
        nuevo=[]
        A=[]
        B=[]
        print(nuevo)
        for j in range(0,5):
            num=int(input("Ingrese un numero: "))
            nuevo.append(num)
        for j in nuevo:
            if j>=0:
                A.append(j)
            else:
                B.append(j)
        print("Los numeros positivos son: {}".format(A))
        print("Los numeros negativos son: {}".format(B))
arry=ejercicio17()
arry.vector()