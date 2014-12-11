class Login:

    def verificar(self, usuario, contrasena):
        usuarios = {"juanPerez":"cartmancuco","sodelVazquez":"pruebasymantenimiento"}       
        if usuario in usuarios:
             return "True"
        else:
             return "False"
