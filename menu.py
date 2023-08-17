#Alejandro León
#Proyecto Final Python
#Happy Burger
#12 de Agosto de 2023
import sqlite3

conn = sqlite3.connect("restaurantehappypizza.db", check_same_thread=False)

class ManejoMenu:
    '''Aqui hacemos la coneccion a la Base de Datos'''
    def __init__(self):
        self.conexion = sqlite3.connect("restaurantehappypizza.db", check_same_thread=False)
        self.cursor = self.conexion.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Menu (
            clave TEXT PRIMARY KEY,
            nombre TEXT,
            precio REAL
        )''')
        self.conexion.commit()

    def agregar_producto(self, clave, nombre, precio):
        '''Aqui hacemos el agregado de los productos a la base de datos, conectando
        a la base de datos, si tienen error imprimi error al agregar al producto'''
        try:
            self.cursor.execute('''INSERT INTO Menu (clave, nombre, precio) VALUES (?, ?, ?)''', (clave, nombre, precio))
            self.conexion.commit()
            print("Producto agregado con éxito.")
        except sqlite3.Error as error:
            print("Error al agregar el producto:", error)

    def eliminar_producto(self, clave):
        '''Aquí llevamos a cabo la eliminación de los productos de la base de datos'''
        try:
            self.cursor.execute('''DELETE FROM Menu WHERE clave = ?''', (clave,))
            self.conexion.commit()
            print("Producto eliminado con éxito.")
        except sqlite3.Error as error:
            print("Error al eliminar el producto:", error)

    def actualizar_producto(self, clave, nombre, precio):
        '''Aquí hacemos una actualización de nuestros productos'''
        try:
            self.cursor.execute('''UPDATE Menu SET nombre = ?, precio = ? WHERE clave = ?''', (nombre, precio, clave))
            self.conexion.commit()
            print("Producto actualizado con éxito.")
        except sqlite3.Error as error:
            print("Error al actualizar el producto:", error)

    def mostrar_menu(self):
        '''Aquí hacemos un fetchall, o sea traer todos, para imprimir en pantalla todo el menú
        esto a través de de un ciclo for que recorre e imprime todos los elementos de la BD'''
        self.cursor.execute('''SELECT * FROM Menu''')
        menu = self.cursor.fetchall()
        print("Menú:")
        for producto in menu:
            print(f"Clave: {producto[0]}")
            print(f"Nombre: {producto[1]}")
            print(f"Precio: ${producto[2]:.2f}")
            print("-" * 30)

    def cerrar_conexion(self):
        '''Aquí hacemos un cierre de la conección'''
        self.conexion.close()

if __name__ == "__main__":
    print("Este archivo no debe ejecutarse directamente.")
