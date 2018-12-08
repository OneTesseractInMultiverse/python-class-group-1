from pymongo import MongoClient
import pprint


client = MongoClient('mongodb://greencore:greencore123@ds111319.mlab.com:11319/greencorelab')

data = [
    {
        'email': 'JOAN.PEREZ@EXAMPLE.COM',
        'id': 'A1S2D6',
        'last_name': 'PEREZ',
        'name': 'JOAN'
    },
    {
        'email': 'JANE.SMITH@EXAMPLE.COM',
        'id': 'A1S27',
        'last_name': 'SMITH',
        'name': 'JANE'
    }
]

# Creo una base de datos
db = client['greencorelab']

# creo una colección de documentos que van a representar personas
persons = db['persons']

for person in data:
    print(persons.insert_one(person).inserted_id)



pprint.pprint(persons.find_one({"id": "A1S27"}))

