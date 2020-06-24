import os

from Bio import Seq,SeqIO
from Bio.Seq import Seq

def dir_maker(folder_name):
	"""
	Funcion que genera las distintas carpetas donde se almacenaran tanto los
	datos input como los datos del output. Siempre y cuando no exista ya una
	una carpeta con el mismo nombre
	"""

	try: #Control carpeta no exista ya
		os.mkdir("./Data/" + folder_name)
		os.mkdir("./Results/" + folder_name)

	except FileExistsError:
		print("El nombre seleccionado para los directorios ya existe, seleccione"
			  " un nombre distinto.\n")
		print ("Usage: python3 main.py [Output folder name] "
			   "[Coverage-cutoff](opcional) [identity_cutoff](opcional)")
		print("\nSi necesita ayuda use el comando -h o -help")
		exit()
	#Generación distintas carpetas
	os.mkdir("./Data/" + folder_name + "/Query")
	os.mkdir("./Data/" + folder_name + "/Subject")
	os.mkdir("./Results/" + folder_name + "/Blast")
	os.mkdir("./Results/" + folder_name + "/Muscle")
	os.mkdir("./Results/" + folder_name + "/Pre_muscle")
	os.mkdir("./Results/" + folder_name + "/Domains")

	return




def query_parser(folder_name, data_dir = r'./Data/Query/'):
	"""
	Funcion para parsear el multifasta o los fasta individuales que se
	introduzcan como query. Separandolos en fastas individuales e 
	introduciendolos en la carpeta correspondiente
	"""
	#Control que el formato sea correcto
 
	for file in os.listdir(data_dir):
		with open(data_dir + file, 'r') as input_handle:
			for record in SeqIO.parse(input_handle, "fasta"): 
				#Un archivo por record del multi fasta
				with open("./Data/" + folder_name + "/Query/" + 
					      record.id, 'a') as f:

					f.write(">" + record.id + "\n")
					f.write(str(record.seq))
					f.close()


	return

def subject_parser(folder_name, data_dir = r'./Data/Subject/'):
	"""
	Funcion para parsear los GenBank que se introduzcan como Subject. 
	Fusionandolos para formar un unico archivo multifasta
	"""
	#Control que el formato sea correcto
	
	for file in os.listdir(data_dir):
		with open(data_dir + file, 'r') as input_handle:
			for record in SeqIO.parse(input_handle, "genbank"):
				with open("./Data/" + folder_name + "/Subject/" + 
						  "Subject_db", 'a') as f: 
				#Todo a un mismo archivo
					for feature in record.features:
						if feature.type == "CDS":

							try: #Se saltan aquellos CDS que falte algun componente
								locus_tag = feature.qualifiers["locus_tag"][0]
								seq = feature.qualifiers["translation"][0]

								f.write(">" + locus_tag + "@" + record.id + "\n")
								f.write(seq + "\n\n")
							except:
								continue
				
				f.close()

	return