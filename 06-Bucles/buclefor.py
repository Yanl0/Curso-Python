contador = 0

for contador in range(0,5):
    print("Voy por el " + str(contador))

#Ejemplo tabla de multiplicar
print("\n ############# EJEMPLO ############")
numero_usuario = int(input("De que numero quieres que muestre la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"Tabla de multiplicar del numero {numero_usuario}")

for numero_tabla in range(0,11):
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada.")