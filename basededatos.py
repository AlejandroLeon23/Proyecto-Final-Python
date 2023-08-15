


import sqlite3

# Crear o conectar a la base de datos
conexion = sqlite3.connect("restaurantehappypizza.db")
cursor = conexion.cursor()

# Crear la tabla de Clientes
cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                    clave TEXT PRIMARY KEY,
                    nombre TEXT,
                    direccion TEXT,
                    correo_electronico TEXT,
                    telefono TEXT
                )''')

# Crear la tabla de Menú
cursor.execute('''CREATE TABLE IF NOT EXISTS Menu (
                    clave TEXT PRIMARY KEY,
                    nombre TEXT,
                    precio REAL
                )''')

# Crear la tabla de Pedido
cursor.execute('''CREATE TABLE IF NOT EXISTS Pedido (
                    numero_pedido INTEGER PRIMARY KEY,
                    cliente TEXT,
                    producto TEXT,
                    precio REAL,
                    FOREIGN KEY (cliente) REFERENCES Clientes(clave),
                    FOREIGN KEY (producto) REFERENCES Menu(clave)
                )''')

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos creada exitosamente.")
