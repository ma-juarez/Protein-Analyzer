import os

def arg_control(num_arg):
	"""
	Funcion para controlar que el numero de argumentos sea el adecuado y que los 
	archivos input sean del tipo adecuado
	"""

	if num_arg < 2:
		print("El número de argumentos introducido no concuerda con lo esperado."
			  " Revise los argumentos introducidos.")
		print("Si necesita ayuda puede usar el comando -h o -help")
		exit()
	elif len(os.listdir("./Data/Query")) == 0:
		print("No se ha introducido ningun archivo como Query. Compruebe que en"
			  " la carpeta ./Data/Query se encuentra el archivo o los archivos "
			  "multifasta o fasta")
		print("Si necesita ayuda consulte el comando -h o -help")
		exit()
	elif len(os.listdir("./Data/Subject")) == 0:
		print("No se ha introducido ningun archivo como Subject. Compruebe que en"
			  " la carpeta ./Data/Subject se encuentra el archivo o los archivos "
			  "GenBank")
		print("Si necesita ayuda consulte el comando -h o -help")
		exit()
	elif len(os.listdir("./Data/Domain_DB")) == 0:
		print("No se ha introducido ningun archivo como Domain_DB. Compruebe que "
			  "en la carpeta ./Data/Domain_DB se encuentra el archivo o los "
			  "archivos .dat de Prosite ")
		print("Si necesita ayuda consulte el comando -h o -help")
		exit()
