import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("\nDe acuerdo!!, vamos a registrarte.")
        nombre = input("Cual es tu nombre?: ")
        apellidos = input("Cuales son tus apellidos?: ")
        email = input("Introduze tu email: ")
        password = input("Introduze tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con {registro[1].email}")
        else:
            print("No te has registrado correctamente")
    
    def login(self):
        print("\n Indentificate.")
        email = input("Introduze tu email: ")
        password = input("Introduze tu contraseña: ")