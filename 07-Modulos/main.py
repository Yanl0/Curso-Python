'''
Modulos: son funcionalidades ya hechas para reutilizar.
Podemos conseguir modulos que bienen en el lenguaje, 
modulos de internet y nuestros propios modulos.
'''
#Importar el modulo propio
#import mimodulo
#from mimodulo import holamundo
from mimodulo import *
#print(mimodulo.holamundo("Juan Luis Garcia Braza"))
print(holamundo("Juan Luis Garcia Braza"))

# Modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
fecha_personalizada = fecha_completa.strftime("%d/%m/%y, %H:%M:%S")
print("Mi fecha personalizada -->", fecha_personalizada)

# Modulo matematicas
import math

print("Raiz cuadrada de 10:", math.sqrt(10))
print("Numero pi: ", math.pi)
print("Redondear: ", math.ceil(6.4678)) #floor

# Modulo random
import random
print("Un numero random entre 1 y 5: ", random.randrange(1,5))