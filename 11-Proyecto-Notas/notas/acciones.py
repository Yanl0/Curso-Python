import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"{usuario[1]}!! Vamos a crear una nueva nota.")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introdice el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Perfecto has guardado correctamente la nota: {nota.titulo}")
        else:
            print(f"No se ha guardado la nota {usuario[1]}")
        
    def mostrar(self, usuario):
        print(f"Vale {usuario[1]}!! Aqui estan tus notas: ")
        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()

        print(notas)

        for nota in notas:
            print("================================")
            print(nota[2])
            print(nota[3])
            print("================================")