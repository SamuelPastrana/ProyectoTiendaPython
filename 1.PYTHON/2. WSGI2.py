# -*- coding: utf-8 -*-
# En este segundo ejemplo utilizaremos el diccionario environ, el diccionario tiene un elemento que se llama PATH_INFO que nos trae la informacion de la ruta a la que estamos accediendo
# En este caso vamos a hacer un programa que determine que ruta estamos obteniendo y segun la ruta de un mensaje de respuesta o de otro.

def application(environ, start_response):
	if environ ["PATH_INFO"] == "/":
	   	respuesta = "<p> TIENDA OFICIAL PASTEUR</p>"
	elif environ ["PATH_INFO"] == "/medicamentos":
		respuesta = "<p> TIPO DE MEDICAMENTOS</p>"
	else:
		respuesta = "<p> PAGINA NO ENCONTRADA</p>"
	start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
	return respuesta


if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	srv = make_server('localhost', 8080, application)
	srv.serve_forever()