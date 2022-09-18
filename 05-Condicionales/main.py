"""
#Operadores de comparacion
== igual
!= distinto
< menor que
> mayor que
>= mayor igual que
<= menor igual que

#Operadores logicos
and Y
or O
! negacion
not no
"""
#Ejemplo 1
print("##### Ejemplo 1 ######")
color = "rojo"

if color == "rojo": 
    print("El color es rojo")
else:
    print("El color no es rojo")

#Ejemplo 2
print("\n#########Ejemplo 2#########")
year = 2022

if year >= 2022:
    print("Estamos de 2022 en adelante")
else:
    print("Es un año anterior a 2022")

#Ejemplo 3
print("\n############Ejemplo 3###########")

nombre = "Juan Luis"
ciudad = "Arcos"
continente = "Europa"
edad = "20"
mayoria_edad = "18"

if edad >= mayoria_edad:
    print(f"{nombre} Es mayor de edad")

    if continente != "Europa":
        print("El usuario no es europeo")
    else:
        print(f"El usuario es europeo y de ciudad {ciudad}")

else:
    print(f"{nombre} No es mayor de edad.")

#Ejemplo 4
print("\n ########Ejemplo4############")
dia = 8

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else: 
    print("Es fin de semana")

#Ejemplo 5
print("\n ########Ejemplo5############")

edad_minima = 18
edad_maxima = 65
edad_oficial = 19

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar!!")
else:
    print("No esta en edad de trabajar!!")

#Ejemplo 6
print("\n ########Ejemplo6############")