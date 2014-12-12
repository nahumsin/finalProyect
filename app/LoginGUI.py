# -*- coding: utf-8 -*-
from Tkinter import Label, Entry, Frame, Tk
from Login import Login


class LoginGUI:
    global usuario, contrasena, message
    root = Tk()
    root.title("Login")
    frame = Frame(root)

    def callback():
        login = Login()
        username = usuario.get()
        password = contrasena.get()
        if login.verificar(username, password) == "True":
            message.configure(text="Bienvenido")
            from AltasBajasGUI import AltasGUI
        else:
            message.configure(
                text="Nombre de usuario o contraseña incorrectos")

    userTitle = Label(frame, text="---Nombre de Usuario---")
    passTitle = Label(frame, text="---Contraseña--")
    message = Label(frame)
    usuario = Entry(frame)
    contrasena = Entry(frame, show='*')

    frame.pack()
    userTitle.pack()
    usuario.pack()
    passTitle.pack()
    contrasena.pack()
    message.pack()

    button = Button(frame, command=callback, text="Log in!")
    button.pack()
    root.mainloop()
