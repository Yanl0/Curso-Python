import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nDe acuerdo!!, vamos a registrarte.")
        nombre = input("Cual es tu nombre?: ")
        apellidos = input("Cuales son tus apellidos?: ")
        email = input("Introduze tu email: ")
        password = input("Introduze tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        #print(registro)

        #registro[0] contiene el numero de lineas que se han escrito en la BD y registro[1] contiene el objeto usuario
        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con {registro[1].email}")
        else:
            print("No te has registrado correctamente")
    
    def login(self):
        print("\n Indentificate.")
        try:
            email = input("Introduze tu email: ")
            password = input("Introduze tu contraseña: ")

            usuario = modelo.Usuario("", "", email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]} te has registrado correctamente -> {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Login incorrecto!!")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear notas (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
        """)

        accion = input("Que quieres hacer?")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            print("Vamos a eliminar")
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"ok {usuario[1]} hasta pronto.")
            exit()
