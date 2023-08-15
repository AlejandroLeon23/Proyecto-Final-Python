#Alejandro León
#Proyecto Final Python
#Happy Burger
#12 de Agosto de 2023

class ManejoClientes:
    def __init__(self):
        self.clientes = {}

    def agregar_cliente(self, clave, nombre, direccion, correo, telefono):
        if clave not in self.clientes:
            self.clientes[clave] = {
                'nombre': nombre,
                'direccion': direccion,
                'correo_electronico': correo,
                'telefono': telefono
            }
            print("Cliente agregado con éxito.")
        else:
            print("Ya existe un cliente con esta clave.")

    def eliminar_cliente(self, clave):
        if clave in self.clientes:
            del self.clientes[clave]
            print("Cliente eliminado con éxito.")
        else:
            print("No se encontró ningún cliente con esta clave.")

    def actualizar_cliente(self, clave, nombre, direccion, correo, telefono):
        if clave in self.clientes:
            self.clientes[clave] = {
                'nombre': nombre,
                'direccion': direccion,
                'correo_electronico': correo,
                'telefono': telefono
            }
            print("Cliente actualizado con éxito.")
        else:
            print("No se encontró ningún cliente con esta clave.")

    def mostrar_clientes(self):
        print("Lista de clientes:")
        for clave, cliente in self.clientes.items():
            print(f"Clave: {clave}")
            print(f"Nombre: {cliente['nombre']}")
            print(f"Dirección: {cliente['direccion']}")
            print(f"Correo electrónico: {cliente['correo_electronico']}")
            print(f"Teléfono: {cliente['telefono']}")
            print("-" * 30)

def main():
    manejador = ManejoClientes()

    while True:
        print("1. Agregar cliente")
        print("2. Eliminar cliente")
        print("3. Actualizar cliente")
        print("4. Mostrar clientes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clave = input("Ingrese la clave del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            direccion = input("Ingrese la dirección del cliente: ")
            correo = input("Ingrese el correo electrónico del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            manejador.agregar_cliente(clave, nombre, direccion, correo, telefono)
        elif opcion == "2":
            clave = input("Ingrese la clave del cliente a eliminar: ")
            manejador.eliminar_cliente(clave)
        elif opcion == "3":
            clave = input("Ingrese la clave del cliente a actualizar: ")
            nombre = input("Ingrese el nuevo nombre del cliente: ")
            direccion = input("Ingrese la nueva dirección del cliente: ")
            correo = input("Ingrese el nuevo correo electrónico del cliente: ")
            telefono = input("Ingrese el nuevo teléfono del cliente: ")
            manejador.actualizar_cliente(clave, nombre, direccion, correo, telefono)
        elif opcion == "4":
            manejador.mostrar_clientes()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
