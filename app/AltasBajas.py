from Paciente import Paciente
class AltasBajas:
    pacientes = {}
    folio = 100
    def alta(self, nombre, apellido, edad, email, direccion):
        paciente = Paciente()
        paciente.setNombre(nombre)
        paciente.setApellido(apellido)
        paciente.setEdad(edad)
        paciente.setEmail(email)
        paciente.setDireccion(direccion)
        paciente.setFolio(self.folio)
        
        self.pacientes.setdefault(str(self.folio),paciente)
        self.folio+1
        return "Paciente agregado"
        
    def baja(self, folio):
        del self.pacientes[folio]
        return "Paciente eliminado"                                               
    
