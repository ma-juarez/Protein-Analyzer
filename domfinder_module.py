import os
import re

from Bio.ExPASy import Prosite
from Bio import Seq,SeqIO
from Bio.Seq import Seq

def finder_filemaker(folder_name):
	"""
	Funcion para generar los archivos con las secuencias completas sobre las que
	se realizara la busqueda de dominios
	"""
	os.mkdir("./Results/" + folder_name + "/Domains/tmp")
	#Adicion secuencias Query
	for file in os.listdir(r'./Data/' + folder_name + '/Query/'):
		os.system("cp ./Data/" + folder_name + "/Query/" + file + " ./Results/" 
				  + folder_name + "/Domains/tmp/" + file + "_tmp")

	#Metodo index para evitar problemas de memoria al parsear la subject db
	fullprot_dict = SeqIO.index("./Data/" + folder_name + "/Subject/Subject_db",
							    "fasta")

	#Adicion secuencias que tienen mismo ID que resultados Blast
	for file in os.listdir("./Results/" + folder_name + "/Muscle/Allignments"):
		with open("./Results/" + folder_name + "/Muscle/Allignments/" + file, 
				  'r') as input_handle:
			for protein in SeqIO.parse(input_handle, "fasta"):
				with open("./Results/" + folder_name + "/Domains/tmp/" 
				  + file.replace("_allignment", "") + "_tmp", 'a') as f:
					if protein.id != file.replace("_allignment", ""):
						f.write("\n" + fullprot_dict[protein.id].format("fasta") 
								+ "\n")

def finder(folder_name):
	"""
	Funcion para compara los dominios de la base de datos con las distintas 
	proteínas. Se itera para cada alineamiento independientemente
	"""
	
	#Cabecera archivos resultados
	for file in os.listdir("./Results/" + folder_name + "/Domains/tmp"):
		with open("./Results/" + folder_name + "/Domains/" 
				  + file.replace("_tmp", "") + "_domains", 'a') as f:
			f.write("Domain Name\tDomain Accession\tDomain Description\t"
					"Domain Pattern\t Protein ID\tPosition\n")


		with open("./Results/" + folder_name + "/Domains/tmp/" + file, 
				  'r') as input_handle:
			#Iteracion en cada proteina
			for protein in SeqIO.parse(input_handle, "fasta"):
				seq_re = str(protein.seq)

				handle = open("./Data/Domain_DB/prosite.dat", "r")
				domains = Prosite.parse(handle)

				#Iteracion sobre cada dominio
				for domain in domains:
					pattern_pro = domain.pattern
					pattern_re = (pattern_pro.replace(".","").replace("x",".")
								 .replace("{","[^").replace("}","]").replace("(","{")
								 .replace(")","}").replace("<","^").replace(">","$")
								 .replace("-",""))
					
					#Busqueda patron en secuencia
					if pattern_re != "" and re.search(pattern_re, seq_re):
						
						with open("./Results/" + folder_name + "/Domains/" 
			  					  + file.replace("_tmp", "") 
			  					  + "_domains", 'a') as f:

							f.write("\n" + domain.name + "\t" + domain.accession 
									+ "\t" + domain.description + "\t" 
									+ domain.pattern + "\t" + protein.id + "\t")

							for m in re.finditer(pattern_re, seq_re):
								f.write(str(m.span()))

		os.remove("./Results/" + folder_name + "/Domains/tmp/" + file)
		input_handle.close()
	f.close()
	os.rmdir("./Results/" + folder_name + "/Domains/tmp")

	return