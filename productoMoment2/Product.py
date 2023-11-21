from Dbconexion import create_connection, close_connection

class Product:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, value):
        self.__codigo = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, value):
        self.__precio = value

    def add_product(self):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO productos (codigo, nombre, precio) VALUES (%s, %s, %s)",
                           (self.codigo, self.nombre, self.precio))
            connection.commit()
            print(f"Producto registrado exitosamente: Código {self.codigo}, Nombre {self.nombre}")

        except Exception as e:
            print("Error al registrar el producto:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    def list_products(self):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT codigo, nombre, precio FROM productos")
            products = cursor.fetchall()

            if products:
                print("Lista de productos:")
                for product in products:
                    code, name, price = product
                    print(f"Código: {code}, Nombre: {name}, Precio: {price}")
            else:
                print("No hay productos registrados en la base de datos.")

        except Exception as e:
            print("Error al listar productos:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

# Callback y Lambda en Product
product_callback = lambda x: print(f"Producto creado con éxito: {x}")

if __name__ == "__main__":
    product = Product(codigo=101, nombre="Nuevo Producto", precio=49.99)
    product.add_product()
    product.list_products()
    product_callback(product.nombre)