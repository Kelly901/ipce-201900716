from flask import Flask, request, jsonify
from Alumno import Alumno
from flask_cors import CORS
app = Flask(__name__)

alumno = Alumno(201900716,"Kelly")
def dump(self):

		return{

			'carnet' : "201900716",
			'nombre' : "Kelly"
		}	

@app.route('/login',methods=['GET'])

def login():

	if request.method == 'GET':

		return dump()		
		
	
	


@app.route("/")
def index():
	nombre = miUsuario[0].usuario
	return nombre

if __name__ == "__main__":
	app.run(threaded=True,port=5000,debug=True)