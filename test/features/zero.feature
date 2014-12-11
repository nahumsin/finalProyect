# -*- coding: utf-8 -*-
# language: es

Funcionalidad: El paciente introduce un nombre de usuario y contraseña y si está
   registrado ingresa al sistema, si no se rechaza el ingreso

Escenario: Ingreso usuario correcto
    Dado un usuario "juanPerez" y una contraseña "cartmancuco"
    Cuando son correctos
    Entonces se muestra un mensaje de "True"

Escenario: Ingreso usuario incorrecto
    Dado un usuario "soyFalso" y una contraseña "noExisto"
    Cuando son correctos
    Entonces se muestra un mensaje de "False"


