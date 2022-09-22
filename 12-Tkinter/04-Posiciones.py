from tkinter import *

ventana = Tk()
#ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa.")
texto.config(
    fg="white",
    bg="black",
    padx=50,
    pady=20,
    font=("Arial", 30)
)
texto.pack(side=TOP)


texto = Label(ventana, text="Soy Juan Luis.")
texto.config(
    height=2,
    bg = "orange",
    font = ("arial", 18),
    padx = 10,
    pady = 7,
    cursor="circle"
)
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text="Texto Basico 1")
texto.config(
    height=5,
    bg = "green",
    font = ("arial", 18),
    padx = 10,
    pady = 7,
    cursor="circle"
)
texto.pack(side=LEFT, fill = X, expand=YES)

texto = Label(ventana, text="Texto Basico 2")
texto.config(
    height=5,
    bg = "blue",
    font = ("arial", 18),
    padx = 10,
    pady = 7,
    cursor="circle"
)
texto.pack(side=LEFT, fill = X, expand=YES)

texto = Label(ventana, text="Texto Basico 3")
texto.config(
    height=5,
    bg = "grey",
    font = ("arial", 18),
    padx = 10,
    pady = 7,
    cursor="circle"
)
texto.pack(side=LEFT, fill = X, expand=YES)

ventana.mainloop()