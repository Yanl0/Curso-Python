from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x700")

Label(ventana, text="Hola soy JuanLuis").pack(anchor=W)

imagen = Image.open('./12-Tkinter/imagenes/goku.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()