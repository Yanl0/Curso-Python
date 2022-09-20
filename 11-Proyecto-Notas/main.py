"""
- Abrir asistente
- Login o registro
- Si elegimos resgistro creara un usuario en bd
- Si elegimos login identificara el usuario y preguntara
- Crear notas, mostrar nostas, borrar notas.
"""

from usuarios import acciones

print("""
Acciones disponibles:
    - registro
    - login
""")

hazEl = acciones.Acciones()
accion = input("Que quiere hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()