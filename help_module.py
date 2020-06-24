
def help_message():
	"""
	Funcion para mostrar el mensaje de ayuda
	"""
	print("Este es un paquete que permite realizar un análisis sobre diversas " 
		  "proteínas. Realiza un blastP entre secuencias query y subject y "
		  "lleva a cabo un alineamiento de las secuencias, generando un arbol "
		  "filogenético. Sumado a esto también se lleva a cabo una búsqueda"
		  " de dominios en las distintas proteínas a partir de una base de datos"
		  " de Prosite\n")
	print("Usage: python3 main.py [Coverage-cutoff](Opcional) "
		  "[Identity-Cutoff](Opcional)\n")
	print("-Archivos Query: Estos irán en la carpeta /Data/Query en formato "
		  "fasta o multifasta")
	print("-Archivos Subject: Estos irán en la carpeta /Data/Subject en formato "
		  "GenBank")
	print("-Archivos Domain DataBase: Estos irán en la carpeta /Data/Domain_DB en "
	      "formato .dat de Prosite")
	print("-Coverage Cutoff: Este parámetro puede ser definido opcionalmente por el "
		  "usuario. Por defecto vendrá definido como 50")
	print("-Identity Cutoff: Este parámetro puede ser definido opcionalmente por el "
		  "usuario. Por defecto vendrá definido como 25")
	print("-Graficación: Es una opción que se le preguntara al usuario. "
		  "Esto incrementara el tiempo de ejecución considerablemente.")


	return