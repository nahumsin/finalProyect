class Paciente:

    def __init__(self):
        self.folio = 0
        self.nombre = ""
        self.apellido = ""
        self.edad = ""
        self.email = ""
        self.direccion = ""

    def setFolio(self, folio):
        self.folio = folio

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setEdad(self, edad):
        self.edad = edad

    def setEmail(self, email):
        self.email = email

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getFolio(self):
        return self.folio

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getEdad(self):
        return self.edad

    def getEmail(self):
        return self.email

    def getDireccion(self):
        return self.direccion
