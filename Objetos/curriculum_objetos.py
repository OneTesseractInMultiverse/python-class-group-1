
# Definición básica de una clase
# Los nombres de las clases son lo único que utiliza CamelCase
class Estudio(object):
    
    # Constructor en Python (__init__)
    # Los constructores son los métodos que utilizamos para crear instancias
    # a poartir de una clase. Y son los que realizar la inicialización.
    # El constructor tiene como responsabilidad realizar la inicialización
    # de una clase. 
    def __init__(self, institution, completed, degree, year_of_completion):

        # Acá en esta sección creamos la definición de los atributos de la clase
        self.__institution = institution
        self.__completed = completed
        self.__degree = degree
        self.__year_of_completion = year_of_completion

    def as_diccionary(self):
        return {
            "institution": self.__institution,
            "completed": self.__completed, 
            "degree": self.__degree, 
            "year_of_completion": self.__year_of_completion
        }
    
    def set_as_incomplete(self):
        self.__completed = False

# Estoy creando una instancia de Estudio a partir de la clase Estudio
estudio_en_harvard = Estudio(
    institution= "Harvard", 
    completed=True, 
    degree="Bachelor Degree in Physics", 
    year_of_completion=2018
)

print(estudio_en_harvard.as_diccionary())
estudio_en_harvard.set_as_incomplete()
print(estudio_en_harvard.as_diccionary())
"""
curriculum = {
    "name": "John", 
    "last_name": "Smith",
    "age": 37, 
    "email": "john.smith@example.com",
    "education": [
        {
            "instituion": "Super High School", 
            "completed": True,
            "degree": "Bachillerado en Educación Media", 
            "year_of_completion": 2002
        },
        {
            "instituion": "University of California in Berkeley", 
            "completed": True,
            "degree": "Bachellor Degree Applied Mathematics", 
            "year_of_completion": 2006
        },
        {
            "instituion": "Harvard University", 
            "completed": True,
            "degree": "Master of Science in Data Science", 
            "year_of_completion": 2009
        }
    ],
    "experience": [
        {
            "company": "GladOS Research Lab",
            "position": "Staff Data Analyst",
            "started": 2007,
            "finished": 2008,
            "actual_job": False,
            "description": "Part of the staff working in diverse revenue leakage tasks"
        },
        {
            "company": "Troogle Inc.",
            "position": "Junior Social Data Analyst",
            "started": 2010,
            "finished": 2013,
            "actual_job": False,
            "description": "Designed algorithms to analyze people's social media and sell them stuff they don't need"
        },
        {
            "company": "Tramazon Corporation",
            "position": "Senior Evil Algorithm Designer",
            "started": 2014,
            "finished": 2018,
            "actual_job": False,
            "description": "Lead the team of Automated Manipulation Algorithms Research Group"
        },
                {
            "company": "Profe en GreenCore",
            "position": "Senior Torturador de Estudiantes",
            "started": 2018,
            "actual_job": True,
            "description": "Atormenta estudiantes con tarea de Python"
        }
    ]
}

# El caso en que el trabajo sea un trabajo pasado
def calcular_años_para_trabajo_finalizado(trabajo):
    return trabajo["finished"] - trabajo["started"]

# EL caso en que el trabajo, sea un trabajo actual
def calcular_años_para_trabajo_actual(trabajo, año_actual):
    return año_actual - trabajo["started"]

# Creo una función coordinadora que me permite coordinar los llamados
# a cada uno de los casos
def obtener_total_años_para_trabajo(trabajo, año_actual):
    if trabajo["actual_job"]:
        return calcular_años_para_trabajo_actual(trabajo, año_actual)
    else:
        return calcular_años_para_trabajo_finalizado(trabajo)


def obtener_cantidad_de_empleos(el_curriculum):
    if "experience" in el_curriculum:
        return len(el_curriculum["experience"])
    else:
        return 0

def obtener_total_años_trabajados(el_curriculum, año_actual, funcion_de_calculo_para_un_trabajo):
    total_años_laborados = 0
    for trabajo in el_curriculum["experience"]:
        total_años_laborados += funcion_de_calculo_para_un_trabajo(trabajo, año_actual)
    return total_años_laborados


print(obtener_cantidad_de_empleos(curriculum))
print(obtener_total_años_trabajados(curriculum, 2020, obtener_total_años_para_trabajo))
"""