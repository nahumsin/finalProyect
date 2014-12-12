# -*- coding: utf-8 -*-
from Tkinter import *
from AltasBajas import AltasBajas


class AltasGUI:
    global nombre, apellidos, edad, email, direccion
    global altasBajas
    altasBajas = AltasBajas()
    root = Tk()
    root.title("Altas")
    frame = Frame(root)

    def callback():
        nombres = nombre.get()
        apellidoss = apellidos.get()
        edads = edad.get()
        emails = email.get()
        direccions = direccion.get()
        altasBajas.alta(nombres, apellidoss, edads, emails, direccions)

    nombreTitle = Label(frame, text="---Nombre---")
    apellidoTitle = Label(frame, text="---Apellido---")
    edadTitle = Label(frame, text="---Edad---")
    emailTitle = Label(frame, text="---Email---")
    direccionTitle = Label(frame, text="---Direccion---")
    message = Label(frame)

    nombre = Entry(frame)
    apellidos = Entry(frame)
    edad = Entry(frame)
    email = Entry(frame)
    direccion = Entry(frame)

    frame.pack()
    nombreTitle.pack()
    nombre.pack()
    apellidoTitle.pack()
    apellidos.pack()
    edadTitle.pack()
    edad.pack()
    emailTitle.pack()
    email.pack()
    direccionTitle.pack()
    direccion.pack()
    message.pack()

    button = Button(frame, command=callback, text="Alta")
    button.pack()
    root.mainloop()
