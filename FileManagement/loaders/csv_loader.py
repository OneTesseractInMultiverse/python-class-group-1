import csv


class CsvLoader(object):

    # ---------------------------------------------------------------
    # CONSTRUCTOR DE LA CLASE
    # ---------------------------------------------------------------
    def __init__(self, file_name):

        # Guardamos el nombre del archivo para que esté disponible para
        # los métodos que lo requieran de esta clase. 
        self.__file_name = file_name

        # Inicializamos una lista vacía como atributo porque necesitamos
        # un lugar para colocar los diccionarios que representan cada una
        # de las filas del archivo CSV
        self.__rows = [] 

        # Ahora leemos el archivo y lo convertimos en una lista de diccionarios
        self.__read_csv_file(self.__file_name)

    # ---------------------------------------------------------------
    # CONSTRUCTOR DE LA CLASE
    # ---------------------------------------------------------------
    def __read_csv_file(self, file_name):
        with open(file_name) as file:
            self.__rows = [{key: value for key, value in row.items()} 
                            for row in csv.DictReader(file, skipinitialspace=True)]

    # ---------------------------------------------------------------
    # ROWS
    # ---------------------------------------------------------------       
    @property
    def rows(self):
        return self.__rows