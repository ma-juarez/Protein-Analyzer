import os

def tree_maker(folder_name):
	"""
	Funcion para realizar el alineamiento de Muscle y el arbol filogenético de 
	forma local
	"""

	#Creacion directorios
	os.mkdir("./Results/" + folder_name + "/Muscle/Allignments")
	os.mkdir("./Results/" + folder_name + "/Muscle/Trees")

	for file in os.listdir("./Results/" + folder_name + "/Pre_muscle/"):

		allign = (" muscle -seqtype protein -in ./Results/" + folder_name 
				  + "/Pre_muscle/" + file + " -out ./Results/" + folder_name 
				  + "/Muscle/Allignments/" + file.replace('_premuscle', '') 
				  + "_allignment -quiet 2> /dev/null")

		try: 
			os.system(allign) #Alineamiento Muscle Local
		except:
			print("No hay resultados con estos parametros para la secuencia" 
				  + file.replace('_premuscle', ''))

	for file in os.listdir("./Results/" + folder_name + "/Muscle/Allignments"):

		tree = (" muscle -maketree -in ./Results/" + folder_name + "/Muscle/" 
				"Allignments/" + file + " -out " + "./Results/" + folder_name 
			   + "/Muscle/Trees/" + file.replace('_allignment', '') 
			   + "_tree -cluster neighborjoining -quiet 2> /dev/null")
		try:
			os.system(tree) #Generación arbol filogenético
		except: 
			print("No hay resultados con estos parametros para la secuencia" 
				  + file.replace('_premuscle', ''))

		
	return


