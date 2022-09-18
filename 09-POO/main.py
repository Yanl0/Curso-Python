from vehiculos import vehiculos
from vehiculos import moto
moto100 = vehiculos("Honda", "CBR", "2", "rojo", "parado")
coche = vehiculos("Toyota", "Supra", "4", "Blanco", "parado")
print(moto100.getInfo())
print(coche.getInfo())

ªmoto1 = moto("Suzuki", "Stars", "2", "azul", "parado")
print(moto1.acelerar())