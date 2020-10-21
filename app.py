from flask import Flask, request, jsonify
from Alumno import Alumno
from flask_cors import CORS
app = Flask(__name__)

alumno = Alumno(201900716,"Kelly")


@app.route('/login',methods=['POST','GET'])

def login():

	if request.method == 'GET':

		nombre=request.form.get('carnet')
		password=request.form.get('nombre')

		for user in miUsuario:

			if user.autenticar(nombre,password)==True:

				return user.dump()

		return "False"		
		
	
	

@app.route("/")
def index():
	nombre = miUsuario[0].usuario
	return nombre

if __name__ == "__main__":
	app.run(threaded=True,port=5000,debug=True)