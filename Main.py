#Alejandro León
#Proyecto Final Python
#Happy Burger
#12 de Agosto de 2023

class happy:
    def menu():
        print("Bienvenidos a Happy Burger \n a continuacion se presenta nuestro Menú digutal")
        print(" a. Pedidos \n b. Clientes \n c. Menú \n d. Salir: ")
        opcion = input("Ingrese la opción Deseada: ").lower()
        return opcion
        
    def Eleccion():
        while True:
            opcion = happy.menu()
            if opcion == ("a"):
                print("Ha seleccionado la opción Pedidos")
                nombre = str(input("Indique el nombre del Producto: "))
                precio = float(input("Indique el precio del producto: "))
                unidades = int(input("Indique la cantidad de Productos: "))
                precioFinal = round((precio * unidades)*1.15)
                print(f"Seleccionó {nombre} y su costo total es de ${precioFinal} IVA incluido")
                continue
            elif opcion == ("b"):
                print("Ha seleccionado la opción Clientes")
                continue
            elif opcion == ("c"):
                print("Ha seleccionado la opción Menú ")
                continue
            elif opcion == ("d"):
                print("Ha seleccionado la opción Salir ")
                break
            else:
                print("No ha elegido una opción válida")
                continue

happy.Eleccion()