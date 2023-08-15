#Alejandro León
#Proyecto Final Python
#Happy Burger
#12 de Agosto de 2023
import sqlite3

class ManejoClientes:
    '''Clase manejo clientes, crea la tabla en caso de que no exista'''
    def __init__(self):
        self.conexion = sqlite3.connect("restaurantehappypizza.db")
        self.cursor = self.conexion.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
            clave TEXT PRIMARY KEY,
            nombre TEXT,
            direccion TEXT,
            correo_electronico TEXT,
            telefono TEXT
        )''')
        self.conexion.commit()

    def agregar_cliente(self, clave, nombre, direccion, correo, telefono):
        '''En esta funcion hacemos un agregado de los clientes'''
        try:
            self.cursor.execute('''INSERT INTO Clientes (clave, nombre, direccion, correo_electronico, telefono)
                                VALUES (?, ?, ?, ?, ?)''', (clave, nombre, direccion, correo, telefono))
            self.conexion.commit()
            print("Cliente agregado con éxito.")
        except sqlite3.Error as error:
            print("Error al agregar el cliente:", error)

    def eliminar_cliente(self, clave):
        '''Eliminación de los clientes, donde con la Clave realizamos el borrado de la BD'''
        try:
            self.cursor.execute('''DELETE FROM Clientes WHERE clave = ?''', (clave,))
            self.conexion.commit()
            print("Cliente eliminado con éxito.")
        except sqlite3.Error as error:
            print("Error al eliminar el cliente:", error)

    def actualizar_cliente(self, clave, nombre, direccion, correo, telefono):
        '''Actualización de los clientes, donde a través de la clave actualizamos los demás
        valores'''
        try:
            self.cursor.execute('''UPDATE Clientes SET nombre = ?, direccion = ?, correo_electronico = ?, telefono = ?
                                WHERE clave = ?''', (nombre, direccion, correo, telefono, clave))
            self.conexion.commit()
            print("Cliente actualizado con éxito.")
        except sqlite3.Error as error:
            print("Error al actualizar el cliente:", error)

    def mostrar_clientes(self):
        '''Aquí realizamos una selección global de la tabla clientes para imprimir a través
        de un ciclo for que realiza un recorrido de todos los valores'''
        self.cursor.execute('''SELECT * FROM Clientes''')
        clientes = self.cursor.fetchall()
        print("Lista de clientes:")
        for cliente in clientes:
            print(f"Clave: {cliente[0]}")
            print(f"Nombre: {cliente[1]}")
            print(f"Dirección: {cliente[2]}")
            print(f"Correo electrónico: {cliente[3]}")
            print(f"Teléfono: {cliente[4]}")
            print("-" * 30)

    def cerrar_conexion(self):
        self.conexion.close()

if __name__ == "__main__":
    print("Este archivo no debe ejecutarse directamente.")

