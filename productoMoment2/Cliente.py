from Dbconexion import create_connection, close_connection


class Customer:
    def __init__(self, id, nombre, correo):
        self.__id = id
        self.__nombre = nombre
        self.__correo = correo

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, value):
        self.__correo = value

    def add_customer(self):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO clientes (id, nombre, correo) VALUES (%s, %s, %s)",
                           (self.id, self.nombre, self.correo))
            connection.commit()
            print(f"Cliente registrado exitosamente: ID {self.id}, Nombre {self.nombre}")

        except Exception as e:
            print("Error al registrar el cliente:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    def list_customers(self):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT id, nombre, correo FROM clientes")
            customers = cursor.fetchall()

            if customers:
                print("Lista de clientes:")
                for customer in customers:
                    customer_id, name, email = customer
                    print(f"ID: {customer_id}, Nombre: {name}, Correo: {email}")
            else:
                print("No hay clientes registrados en la base de datos.")

        except Exception as e:
            print("Error al listar clientes:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

# Callback y Lambda en Customer
customer_callback = lambda x: print(f"Cliente creado con éxito: {x}")

if __name__ == "__main__":
    customer = Customer(id=201, nombre="Nuevo Cliente", correo="nuevo@example.com")
    customer.add_customer()
    customer.list_customers()
    customer_callback(customer.nombre)