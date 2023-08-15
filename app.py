#Alejandro León
#Proyecto Final Python
#Happy Burger
#12 de Agosto de 2023
from flask import Flask, render_template, request
from clientes import ManejoClientes
from menu import ManejoMenu
from pedidos import ManejoPedidos

app = Flask(__name__)

manejador_clientes = ManejoClientes()
manejador_menu = ManejoMenu()
manejador_pedidos = ManejoPedidos()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultar_pedido', methods=['POST'])
def consultar_pedido():
    pedido = request.form['numero_pedido']
    pedido = ManejoPedidos.mostrar_pedidos(pedido)
    return render_template('consulta_pedido.html', pedido=pedido)

if __name__ == '__main__':
    app.run(debug=True)
