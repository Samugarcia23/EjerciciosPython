import Electrodomestico

ob1 = Electrodomestico.Electrodomestico(100, "rojo", 'a', 10)
ob2 = Electrodomestico.Lavadora(10, 200, "blanco", 'b', 20)
ob3 = Electrodomestico.Electrodomestico(300, "gris", 'c', 30)
ob4 = Electrodomestico.Television(50, True,400, "azul", 'd', 40)
ob5 = Electrodomestico.Electrodomestico(500, "blanco", 'e', 50)
ob6 = Electrodomestico.Lavadora(50, 600, "negro", 'f', 60)
ob7 = Electrodomestico.Electrodomestico(700, "rojo", 'f', 70)
ob8 = Electrodomestico.Television(39, True, 800, "blanco", 'e', 80)
ob9 = Electrodomestico.Electrodomestico(900, "negro", 'd', 90)
ob10 = Electrodomestico.Television(60, False, 1000, "rojo", 'a', 100)

my_list=[ob1, ob2, ob3, ob4, ob5, ob6, ob7, ob8, ob9, ob10]

totalElectrodomestico = 0
totalTv = 0
totalLavadora = 0
for e in my_list:
    totalElectrodomestico = totalElectrodomestico + e.precioFinal()
    if type(e) is Electrodomestico.Lavadora:
        totalLavadora = totalLavadora + e.precioFinal()
    elif type(e) is Electrodomestico.Television:
        totalTv = totalTv + e.precioFinal()

print ("Electrodomesticos: "+str(totalElectrodomestico )+ " €")
print ("Lavadoras: "+str(totalLavadora) + " €")
print("Tv: "+str(totalTv) + " €")