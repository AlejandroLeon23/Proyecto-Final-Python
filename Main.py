#Alejandro León
#Proyecto Final Python
#Happy Burger
#12 de Agosto de 2023

from clientes import ManejoClientes
from menu import ManejoMenu
from pedidos import ManejoPedidos

def main():
    manejador_clientes = ManejoClientes()
    manejador_menu = ManejoMenu()
    manejador_pedidos = ManejoPedidos()

    while True:
        print("1. Agregar cliente")
        print("2. Eliminar cliente")
        print("3. Actualizar cliente")
        print("4. Mostrar clientes")
        print("5. Agregar producto")
        print("6. Eliminar producto")
        print("7. Actualizar producto")
        print("8. Mostrar menú")
        print("9. Crear pedido")
        print("10. Cancelar pedido")
        print("11. Mostrar pedidos")
        print("12. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clave = input("Ingrese la clave del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            direccion = input("Ingrese la dirección del cliente: ")
            correo = input("Ingrese el correo electrónico del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            manejador_clientes.agregar_cliente(clave, nombre, direccion, correo, telefono)
        elif opcion == "2":
            clave = input("Ingrese la clave del cliente a eliminar: ")
            manejador_clientes.eliminar_cliente(clave)
        elif opcion == "3":
            clave = input("Ingrese la clave del cliente a actualizar: ")
            nombre = input("Ingrese el nuevo nombre del cliente: ")
            direccion = input("Ingrese la nueva dirección del cliente: ")
            correo = input("Ingrese el nuevo correo electrónico del cliente: ")
            telefono = input("Ingrese el nuevo teléfono del cliente: ")
            manejador_clientes.actualizar_cliente(clave, nombre, direccion, correo, telefono)
        elif opcion == "4":
            manejador_clientes.mostrar_clientes()
        elif opcion == "5":
            clave = input("Ingrese la clave del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            manejador_menu.agregar_producto(clave, nombre, precio)
        elif opcion == "6":
            clave = input("Ingrese la clave del producto a eliminar: ")
            manejador_menu.eliminar_producto(clave)
        elif opcion == "7":
            clave = input("Ingrese la clave del producto a actualizar: ")
            nombre = input("Ingrese el nuevo nombre del producto: ")
            precio = float(input("Ingrese el nuevo precio del producto: "))
            manejador_menu.actualizar_producto(clave, nombre, precio)
        elif opcion == "8":
            manejador_menu.mostrar_menu()
        elif opcion == "9":
            cliente_clave = input("Ingrese la clave del cliente: ")
            producto_clave = input("Ingrese la clave del producto: ")
            manejador_pedidos.crear_pedido(cliente_clave, producto_clave)
        elif opcion == "10":
            numero_pedido = int(input("Ingrese el número de pedido a cancelar: "))
            manejador_pedidos.cancelar_pedido(numero_pedido)
        elif opcion == "11":
            manejador_pedidos.mostrar_pedidos()
        elif opcion == "12":
            manejador_clientes.cerrar_conexion()
            manejador_menu.cerrar_conexion()
            manejador_pedidos.cerrar_conexion()
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
