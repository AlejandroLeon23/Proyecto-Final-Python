#Alejandro León
#Proyecto Final Python
#Happy Burger
#12 de Agosto de 2023
import sqlite3

class ManejoPedidos:
    def __init__(self):
        '''Conexión de la base de datos local con sqlite'''
        self.conexion = sqlite3.connect("restaurantehappypizza.db")
        self.cursor = self.conexion.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Pedido (
            numero_pedido INTEGER PRIMARY KEY,
            cliente TEXT,
            producto TEXT,
            precio REAL,
            FOREIGN KEY (cliente) REFERENCES Clientes(clave),
            FOREIGN KEY (producto) REFERENCES Menu(clave)
        )''')
        self.conexion.commit()

    def crear_pedido(self, cliente_clave, producto_clave):
        '''Aquí se crena los pedidos, tomando como referencia las otras dos tablas, menu y clientes
        '''
        try:
            # Obtener el nombre del cliente y el nombre del producto
            self.cursor.execute('''SELECT nombre FROM Clientes WHERE clave = ?''', (cliente_clave,))
            nombre_cliente = self.cursor.fetchone()[0]

            self.cursor.execute('''SELECT nombre, precio FROM Menu WHERE clave = ?''', (producto_clave,))
            nombre_producto, precio_producto = self.cursor.fetchone()

            # Insertar el registro en la tabla Pedido
            self.cursor.execute('''INSERT INTO Pedido (cliente, producto, precio)
                                VALUES (?, ?, ?)''', (nombre_cliente, nombre_producto, precio_producto))
            self.conexion.commit()
            print("Pedido creado con éxito.")
        except sqlite3.Error as error:
            print("Error al crear el pedido:", error)

    def cancelar_pedido(self, numero_pedido):
        '''Aqui hacemos un borrado del pedido realizado, seleccionamos la tabla de pedidos y se borran'''
        try:
            self.cursor.execute('''DELETE FROM Pedido WHERE numero_pedido = ?''', (numero_pedido,))
            self.conexion.commit()
            print(f"Pedido {numero_pedido} cancelado.")
        except sqlite3.Error as error:
            print("Error al cancelar el pedido:", error)

    def mostrar_pedidos(self):
        '''A través de un selectfrom, en este caso de la tabla pedidos y con un ciclo
        for hacemos un recorrido de todos los valores'''
        self.cursor.execute('''SELECT * FROM Pedido''')
        pedidos = self.cursor.fetchall()
        print("Lista de pedidos:")
        for pedido in pedidos:
            print(f"Número de pedido: {pedido[0]}")
            print(f"Cliente: {pedido[1]}")
            print(f"Producto: {pedido[2]}")
            print(f"Precio: ${pedido[3]:.2f}")
            print("-" * 30)

    def cerrar_conexion(self):
        '''Cierre de la conexion a la BD'''
        self.conexion.close()

if __name__ == "__main__":
    print("Este archivo no debe ejecutarse directamente.")
