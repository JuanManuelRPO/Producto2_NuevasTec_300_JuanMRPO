import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="momento2"
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos.")
            return connection
    except Exception as e:
        print("Error al conectar a la base de datos:", str(e))
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("Conexión cerrada.")
