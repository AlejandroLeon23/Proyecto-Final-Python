
import sqlite3

class ManejoMenu:
    def __init__(self):
        self.conexion = sqlite3.connect("restaurantehappypizza.db")
        self.cursor = self.conexion.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Menu (
            clave TEXT PRIMARY KEY,
            nombre TEXT,
            precio REAL
        )''')
        self.conexion.commit()

    def agregar_producto(self, clave, nombre, precio):
        try:
            self.cursor.execute('''INSERT INTO Menu (clave, nombre, precio) VALUES (?, ?, ?)''', (clave, nombre, precio))
            self.conexion.commit()
            print("Producto agregado con éxito.")
        except sqlite3.Error as error:
            print("Error al agregar el producto:", error)

    def eliminar_producto(self, clave):
        try:
            self.cursor.execute('''DELETE FROM Menu WHERE clave = ?''', (clave,))
            self.conexion.commit()
            print("Producto eliminado con éxito.")
        except sqlite3.Error as error:
            print("Error al eliminar el producto:", error)

    def actualizar_producto(self, clave, nombre, precio):
        try:
            self.cursor.execute('''UPDATE Menu SET nombre = ?, precio = ? WHERE clave = ?''', (nombre, precio, clave))
            self.conexion.commit()
            print("Producto actualizado con éxito.")
        except sqlite3.Error as error:
            print("Error al actualizar el producto:", error)

    def mostrar_menu(self):
        self.cursor.execute('''SELECT * FROM Menu''')
        menu = self.cursor.fetchall()
        print("Menú:")
        for producto in menu:
            print(f"Clave: {producto[0]}")
            print(f"Nombre: {producto[1]}")
            print(f"Precio: ${producto[2]:.2f}")
            print("-" * 30)

    def cerrar_conexion(self):
        self.conexion.close()

if __name__ == "__main__":
    print("Este archivo no debe ejecutarse directamente.")
