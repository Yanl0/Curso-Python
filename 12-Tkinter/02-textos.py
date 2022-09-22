from tkinter import *

def pruebas(nombre, apellidos, pais):
     return f"Hola {nombre} {apellidos}, veo que eres de {pais}"


ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa.")
texto.config(
    fg="white",
    bg="black",
    padx=50,
    pady=20,
    font=("Arial", 30)
)
texto.pack()


texto = Label(ventana, text="Soy Juan Luis.")
texto.config(
    height=10,
    bg = "orange",
    font = ("arial", 18),
    padx = 10,
    pady = 7,
    cursor="circle"
)
texto.pack()

texto = Label(ventana, text=pruebas(nombre="Juan Luis", apellidos="Garcia", pais="España"))
texto.config(
    height=10,
    bg = "green",
    font = ("arial", 18),
    padx = 10,
    pady = 7,
    cursor="circle"
)
texto.pack(anchor=NW)

ventana.mainloop()