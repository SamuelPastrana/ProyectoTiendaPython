from flask import Flask
app = Flask(__name__)	

@app.route('/')
def inicio():
    return 'Pagina Principal'

@app.route('/medicamentos/')
def medicamentos():
	return 'Lista De Medicamentos'

@app.route('/precios')
def precios():
	return	'Lista De Precios'

@app.route('/medicamentos/<int:id>')
def mostrar_medicamentos(id):
	return 'Vamos a mostrar el medicamento con id:{}'.format(id)

@app.route('/users/')
@app.route('/users/<string:nombre>')
@app.route('/users/<string:nombre>/<int:edad>')
def hola(nombre=None, edad=None):
	if nombre and edad:
		return 'Hola, {0} tienes {1} años'.format(nombre,edad)
	elif nombre:
		return 'Hola, {0}'. format(nombre)
	else:
		return 'hola usuario'