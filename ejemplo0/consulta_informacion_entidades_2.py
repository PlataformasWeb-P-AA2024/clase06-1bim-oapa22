"""
    Consulta de información en las entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Autor"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()
print(informacion)
# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
for d in informacion:
    print("El nombre es: %s y la edad es %d" % (d[0], d[3]))
    #print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))

#La variable informacion es una lista de tuplas -> [(x), (x)], en el for, d hace refencia a cada tupla, y d[x] hace referencia a la
#posicion del dato que se encuentra en la tupla

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
