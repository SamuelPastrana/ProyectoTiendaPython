#-*- coding: utf-8 -*-
# Debo crear una funcion llamada application, para que la funcion
# sea valida necesita una variable que es un diccionario, environ
# Donde está toda la información de la petición que le llega, hay tenemos informacion de la ruta que se a accedido, 
# El metodo que se ha utilizado en la petición, la informacion las variables que se mandan al servidor
# Luego tiene otro parametro que es una funcion que nos va a permitir generar las respuestas que le vamos a enviar al cliente

def application(environ, start_response):
	# Guardo la salida que devolveré como respuesta
	respuesta = "<p> Tienda Farmaceutica Virtual con <strong> Python!</strong></p>"
	# Se utilzia la funcion start_response para generar los datos de la respuesta, en este caso se envia un codigo de respuesta 200, 
	#va a devolver estas cabeceras y va a devolver la respuesta
	start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
	return respuesta

	# Este codigo python nos va a proporcionar la creación de un servidor web que va a estar escuchando el localhost en el puerto 8080. 
	# Cuando hagamos una peticion a este servidor, va a recibirla nuestra aplicacion WSGI
	# Que lo unico que va a hacer es devolvernos una respuesta con el codigo HTML creado anteriormente
if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	srv = make_server('localhost', 8080, application)
	srv.serve_forever()