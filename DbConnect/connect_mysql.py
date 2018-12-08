import mysql.connector
import pprint


def get_connection():
    cnx = mysql.connector.connect(
        user="mvcr",
        password="Wstinol1a2s3d.!",
        host="dbx.appsecurity.info",
        database="mvcr_dev"
    )
    return cnx, cnx.cursor()

# Declarar una conexión con la base de datos y además obtener
# un cursor que permite iterar por cada uno de los resultados
# de una consulta.

person_name = input("Digite el nombre de la persona que desea buscar: ")

mysql_connection, mysql_cursor = get_connection()
mysql_cursor.execute("SELECT * FROM Person WHERE NAME='{}'".format(person_name.upper()))

persons = mysql_cursor.fetchall()

person_list = []

# El ciclo for va a cargar cada una de las filas que retorna 
# la comnsulta en un diccionario que agregamos a la lista 
# de personas

for person in persons:
    person_list.append({
        "id": person[0], 
        "name": person[1], 
        "last_name": person[2], 
        "email": person[3]
    })

pprint.pprint(person_list)

'''
terms = []
for result in translation_data:
    terms.append({
        "key": result[0],
        "title": result[1]
    })
'''
mysql_cursor.close()
mysql_connection.close()