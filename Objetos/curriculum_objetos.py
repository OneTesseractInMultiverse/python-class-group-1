
# ---------------------------------------------------------------------------
# CLASE ESTUDIO
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# CLASE JOB
# ---------------------------------------------------------------------------
class Job(object):

    def __init__(self,company, position, started, finished, is_actual_job, description):
        self.__company = company
        self.__position = position
        self.__started = started
        self.__finished = finished
        self.__is_actual_job = is_actual_job
        self.__description = description

    def as_dictionary(self):
        return {
            "company": self.__company,
            "position": self.__position,
            "started": self.__started,
            "finished": self.__finished,
            "is_actual_job": self.__is_actual_job,
            "description": self.__description
        }

    def __calculate_experience_when_not_actual_job(self):
        return self.__finished - self.__started
    
    def __calculate_experience_when_actual_job(self, actual_year):
        return actual_year - self.__started

    def get_years_of_experience(self, actual_year):
        if self.__is_actual_job:
            return self.__calculate_experience_when_actual_job()
        else:
            return self.__calculate_experience_when_not_actual_job()



class Curriculum(object):

    def __init__(self, name, last_name, age, email):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__email = email
        self.__education = []
        self.__experience = []
    
    def add_education(self, education):
        if education is not None:
            self.__education.append(education)

    def add_experience(self, job):
        if job is not None:
            self.__experience.append(job)

    def get_total_years_of_experience(self, actual_year):
        total = 0
        for job in self.__experience:
            total += job.get_years_of_experience(actual_year)
        return total


# ---------------------------------------------------------------------------
# ACA YA ESTAMOS FUERA DE CLASE
# ---------------------------------------------------------------------------

curriculum = Curriculum(
    name="John", 
    last_name="Smith", 
    age = 37, 
    email="john.smith@example.com"
)

curriculum.add_experience(Job(
    company="Los Patitos S.A", 
    position="Engineer", 
    started=1980, 
    finished=2007, 
    is_actual_job=False, 
    description="Bug People"
))

print(curriculum.get_total_years_of_experience(2018))


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