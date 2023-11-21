
from Product import Product, product_callback
from Cliente import Customer, customer_callback

if __name__ == "__main__":
    print("Bienvenido al Sistema de Gestión")

    # Uso de clases Product y Customer
    product = Product(codigo=101, nombre="Nuevo Producto", precio=49.99)
    customer = Customer(id=201, nombre="Nuevo Cliente", correo="nuevo@example.com")

    # Uso de métodos de las clases
    product.add_product()
    product.list_products()
    product_callback(product.nombre)

    customer.add_customer()
    customer.list_customers()
    customer_callback(customer.nombre)
