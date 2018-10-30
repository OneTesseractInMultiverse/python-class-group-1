class Persona(object):

    # --------------------------------------------
    # MÉTODO
    # --------------------------------------------

    # CONSTRUCTOR --------------------------------
    # Responsabilidad de un constructor en un objeto
    # es realizar la inicialización
    def __init__(self, nombre, apellido, cedula, edad= None):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.__edad = edad

    @property
    def full_name(self):
        return "{} {}".format(self.nombre, self.apellido)


persona = Persona(
    "Pedro", 
    "Guzmán", 
    "1122334455"
)

print(persona.full_name)
