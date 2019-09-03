from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Página principal'

@app.route('/medicamentos/')
def medicamentos():
    return 'Lista de medicamentos'

@app.route('/medicamentos/news',methods=["POST"])
def medicamentos_new():
	return 'Está URL recibe información de un formulario con el método POST'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Hemos accedido con POST'
    else:
        return 'Hemos accedido con GET'