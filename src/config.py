from psycopg2 import connect

HOST= 'localhost'
PORT= 5432
BD= 'bd_personas'
USUARIO= 'postgres'
PASS= '12345'

def establecerconexion():
    try:
        conexion=connect(host=HOST, port=PORT, dbname=BD, user=USUARIO, password=PASS)
    except ConnectionError:
        print("Error de conexion")

    return conexion
    