from tkinter import *
import os.path

class Programa:
    def __init__(self):
        self.title = "Ventana grafica by Yanl0"
        self.icon = "T:/Master_Python/12-Tkinter/imagenes/logo.ico"
        self.size = "770x470"
        self.resizable = False
    
    def cargar(self):
        #Crear ventana raiz
        ventana = Tk()
        self.ventana = ventana
        #Titulo de la ventana
        ventana.title(self.title)
        #Comprobar si existe un archivo
        ruta_icono = os.path.abspath('./imagenes/logo.ico')
        #MOstrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()
        #Icono de la ventana
        ventana.iconbitmap(self.icon)
        # #Cambiar tamaño de la ventana
        ventana.geometry(self.size)
        #Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        #Arrancar y mostrar la ventana hasta que se cierre.
        self.ventana.mainloop()

#Instanciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto("Hola nuevo texto")
programa.mostrar()




