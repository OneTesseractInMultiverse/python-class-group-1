
class Engine(object):

    # ------------------------------------------------
    # Constructor
    # ------------------------------------------------
    def __init__(self, type, hp, brand):
        self.__type = type # Diesel, Gas, Electric
        self.__hp = hp # Horse Power
        self.__brand = brand
        self.__is_on = False
        self.__rpm = 0 # RPM
    
    @property
    def brand(self):
        return self.__brand

    @property
    def is_on(self):
        # Esto solo retorna el valor. Lo que previente que 
        # alguien más pueda modificar el estado
        return self.__is_on

    # Método para encender el motor si está apagado
    def turn_on(self):
        if not self.is_on:
            self.__is_on = True

    # Método para apagar el motor si está encendido
    def turn_off(self):
        if self.is_on:
            self.__is_on = False


# ----------------------------------------------------------------
# CLASS VEHICLE
# ----------------------------------------------------------------
class Vehicle(object):

    def __init__(self, engine=None, color="grey", make="Tata",
        transmission="manual"):
        self._engine = None
        self._init_engine(engine)
        self.__color = color
        self._make = make
        self.__transmission = transmission

    def _init_engine(self, engine):
        if engine:
            self._engine = engine
        else:
            self._engine = Engine("diesel", 80, "tata")

    def is_on(self):
        return self._engine.is_on

    def turn_on(self):
        self._engine.turn_on()
    
    def turn_off(self):
        self._engine.turn_off()

    def switch_engine(self, engine):
        self._engine = engine

    def get_engine_brand(self):
        return self._engine.brand


class Tank(Vehicle):

    def __init__(self, engine=None, color="grey", make="Tata",
        transmission="manual", caliber=35):
        # Primero llamamos a la lógica de inicialización del padre
        # super == padre
        super().__init__(engine, color, make, transmission)
        self.caliber = caliber
        
    # Acá estamos sobrescribiendo la implementación de este método
    # del padre
    def _init_engine(self, engine):
        if engine:
            self._engine = engine
        else:
            self._engine = Engine("diesel", 500, "Oshkosh")
    
    def shoot():
        return True


car = Tank(engine=None, color='red', make='audi', caliber=90)
if not car.is_on:
    print("El carro está apagado")
# car.switch_engine(Engine('electric', 250, 'Tesla'))
print(car.get_engine_brand())
car.turn_on()
if car.is_on:
    print("El carro está encendido")

