#Alejandro León
#Proyecto Final Python
#Happy Burger
#12 de Agosto de 2023
from flask import Flask, render_template
from pedidos import ManejoPedidos

app = Flask(__name__)

manejador_pedidos = ManejoPedidos()

@app.route('/')
def mostrar_pedidos():
    pedidos = manejador_pedidos.mostrar_pedidos2()
    return render_template('pedidos.html', pedidos=pedidos)

if __name__ == '__main__':
    app.run(debug=True)
