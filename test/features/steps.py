# -*- coding: utf-8 -*-
from lettuce import step, world
from app.Login import Login
from app.AltasBajas import AltasBajas
from app.Paciente import Paciente
@step(u'Dado el numero de folio "([^"]*)"')
def dado_el_numero_de_folio_group1(step, folio):
    world.folio = folio
    
@step(u'Dado un usuario "([^"]*)" y una contraseña "([^"]*)"')
def dado_un_usuario_group1_y_una_contrasena_group2(step, usuario, contrasena):
    world.login = Login()
    world.usuario = usuario
    world.contrasena = contrasena

@step(u'Dado un nombre "([^"]*)" un apellido "([^"]*)" una edad "([^"]*)" un correo "([^"]*)" una dirección "([^"]*)"')
def dado_un_nombre_group1_un_apellido_group2_una_edad_group3_un_correo_group4_una_direccion_group5(step, nombre, apellido, edad, email, direccion):
    world.altasBajas = AltasBajas()
    world.nombre = nombre
    world.apellido = apellido
    world.edad = edad
    world.email = email
    world.direccion = direccion
    
@step(u'Cuando son correctos')
def cuando_son_correctos(step):
    world.result = world.login.verificar(world.usuario,world.contrasena)

@step(u'Cuando se dan de alta')
def cuando_se_dan_de_alta(step):
    world.result = world.altasBajas.alta(world.nombre,world.apellido,world.edad,world.email,world.direccion)

@step(u'Cuando se borra el paciente')
def cuando_se_borra_el_paciente(step):
    world.result = world.altasBajas.baja(world.folio)    
    
@step(u'Entonces se muestra un mensaje de "([^"]*)"')
def entonces_se_muestra_un_mensaje_de_group1(step, resEsperado):
    assert world.result == resEsperado, 'El resultado esperado %s y el esperado es %s' % (world.result, resEsperado)
