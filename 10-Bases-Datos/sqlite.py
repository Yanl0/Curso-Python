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

#Borrar registros
cursor.execute("DELETE FROM productos;")

#Insertar muchos registros de una vez
productos = [
    ("Ordenador portatil", "buen pc", 700),
    ("Telefono movil", "buen movil", 140),
    ("Placa base", "buena placa", 80),
    ("Tablet", "buen tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

#UPDATE
cursor.execute("UPDATE productos SET Precio=123 WHERE Precio=80")
#Listar datos
cursor.execute("SELECT * FROM productos WHERE Precio <= 500;")
productos = cursor.fetchall()
for producto in productos:
    print("---------------------")
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Precio: ", producto[3] )

cursor.execute("SELECT Titulo FROM productos;")
producto = cursor.fetchone()
print(producto)

#Cerrar conexion
conexion.close()
