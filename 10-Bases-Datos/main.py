import mysql.connector

#conexion
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

#comprobar conexion correcta
#print(database)

#Cursor
cursor = database.cursor(buffered=True) #buffered solo si usamos para mas de un cosa el mismo cursor

#Crear la base de datos
'''
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
#Consultar las DB
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)
'''

#Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

#Consultar las tablas
"""
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
"""
#Insertar un dato
#cursor.execute("INSERT INTO vehiculos values(null, 'Opel', 'Astra', 18500)")

coches = [
    ('seat', 'Ibiza', 5000),
    ('renault', 'clio', 15000),
    ('citroen', 'saxo', 2000),
    ('mercedes', 'Clase A', 35000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
database.commit()

#Consultar datos
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'seat'")
result = cursor.fetchall()

print("--------- TODOS MIS COCHES ----------")
for coche in result:
    print(coche[1])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)

#Borrar regsitros
cursor.execute("DELETE FROM vehiculos WHERE marca = 'renault'")
database.commit()
print(cursor.rowcount, "Vehiculos borrados")

#Actualizar
cursor.execute("UPDATE vehiculos SET modelo='leon1' WHERE marca='seat'")
database.commit()
print(cursor.rowcount, "Vehiculos actualizados")