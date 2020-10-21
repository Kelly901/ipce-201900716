class Alumno:

	def __init__(self,carnet,nombre):
		self.carnet=carnet
		self.nombre=nombre


	def autenticar(self,carnet,nombre):

		if self.carnet==carnet and self.nombre==nombre :
			print("El nombre y el carnet coincide")
			return True

		return False

	
		