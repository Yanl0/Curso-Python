from tkinter import *
ventana = Tk()
ventana.title("Marcos | Master en python")
ventana.geometry("700x700")

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue",
    bd=7,
    relief="raised"
)
marco_padre.pack(side=TOP, fill = X, expand=YES, anchor=N)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=7,
    relief="raised"
)
marco.pack(side=LEFT, anchor=SW)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd=7,
    relief="raised"
)
marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue",
    bd=7,
    relief="raised"
)
marco_padre.pack(side=BOTTOM,fill = X, expand=YES, anchor=S)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="blue",
    bd=7,
    relief="raised"
)
marco.pack(side=LEFT)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="yellow",
    bd=7,
    relief="raised"
)
marco.pack(side=RIGHT)

ventana.mainloop()