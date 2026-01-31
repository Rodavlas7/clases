from Vehiculos import Taxi, Autobus

t1 = Taxi("Tsuru","2014",200,1234567890)
t1.agregarViaje(3,150)
t1.agregarViaje(2,120)
t1.agregarViaje(1,50)
t1.agregarViaje(1,40)
t1.info()

print()
print()


b1 = Autobus("Honda 233", "1999", 2000, 30)
b1.info()
print()
b1.subirPersonas(16)
b1.info()
print()
b1.subirPersonas(13)
print()
b1.info()
print()
b1.subirPersonas(2)
print()
b1.info()