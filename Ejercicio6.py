class ejercicio6:
    def __init__(self):
        pass
    
    def horasextras (self):
        horast, pagoh=0,0
        horast=int(input("Ingrese las horas trabajadas: "))
        pagoh=int(input("Ingrese el valor que le pagan por hora: "))
        if horast>40:
            horasex=horast-40
            if horasex>8:
                het=horasex-8
                pagohe=pagoh*2*8+pagoh*3*het
            else:
                pagohe=pagoh*2*horasex
            pagototal=pagoh*40+pagohe
        else:
            pagototal=pagoh*horast
        print("El pago total es de: ",pagototal)
pagoextra=ejercicio6()
pagoextra.horasextras()

        