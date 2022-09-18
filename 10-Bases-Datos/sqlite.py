import sqlite3

conexion = sqlite3.connect('pruebas.db')
#Crear cursor
cursor = conexion.cursor()
#Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"Id INTEGER PRIMARY KEY AUTOINCREMENT," +
"Titulo VARCHAR(255), " +
"Descripcion TEXT, " +
"Precio int(255)"
")")

#Insertar datos
#cursor.execute("INSERT INTO productos VALUES (null, 'Segundo producto', 'Descripcion del producto', 550)")
#conexion.commit()

#Listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
for producto in productos:
    print("---------------------")
    print("Titulo: ", producto[1])
    print("Precio: ", producto[3] )

cursor.execute("SELECT Titulo FROM productos;")
producto = cursor.fetchone()
print(producto)
#Cerrar conexion
conexion.close()
