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

@app.route('/menu')
def mostrar_menu():
    menu = manejador_menu.mostrar_menu()
    return render_template('menu.html', menu=menu)

@app.route('/clientes')
def mostrar_clientes():
    clientes = manejador_clientes.mostrar_clientes()
    return render_template('clientes.html', clientes=clientes)

@app.route('/consultar_pedido', methods=['POST'])
def consultar_pedido():
    numero_pedido = int(request.form['numero_pedido'])
    pedido = manejador_pedidos.consultar_pedido(numero_pedido)
    return render_template('consulta_pedido.html', pedido=pedido)

if __name__ == '__main__':
    app.run(debug=True)
