from tkinter import *

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
texto.pack()

ventana.mainloop()