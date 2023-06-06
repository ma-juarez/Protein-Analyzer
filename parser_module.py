import os

from Bio import Seq,SeqIO
from Bio.Seq import Seq

def dir_maker(folder_name):
	"""
	Funtion that creates the different folders where input and output will be stored. 
	This function will be skipped if a folder with teh same name already exists.
	"""

	try: #Folder conrol
		os.mkdir("./Data/" + folder_name)
		os.mkdir("./Results/" + folder_name)

	except FileExistsError:
		print("El nombre seleccionado para los directorios ya existe, seleccione"
			  " un nombre distinto.\n")
		print ("Usage: python3 main.py [Output folder name] "
			   "[Coverage-cutoff](opcional) [identity_cutoff](opcional)")
		print("\nSi necesita ayuda use el comando -h o -help")
		exit()
	#Folder creation
	os.mkdir("./Data/" + folder_name + "/Query")
	os.mkdir("./Data/" + folder_name + "/Subject")
	os.mkdir("./Results/" + folder_name + "/Blast")
	os.mkdir("./Results/" + folder_name + "/Muscle")
	os.mkdir("./Results/" + folder_name + "/Pre_muscle")
	os.mkdir("./Results/" + folder_name + "/Domains")

	return




def query_parser(folder_name, data_dir = r'./Data/Query/'):
	"""
	Funtion that parses the multifasta or multiple single fasta introduced 
	as query. Sequences are separated into individual fastas and introduced 
	in the respective folder
	"""
	#Format control
 
	for file in os.listdir(data_dir):
		with open(data_dir + file, 'r') as input_handle:
			for record in SeqIO.parse(input_handle, "fasta"): 
				#One file per sequence of multifasta 
				with open("./Data/" + folder_name + "/Query/" + 
					      record.id, 'a') as f:

					f.write(">" + record.id + "\n")
					f.write(str(record.seq))
					f.close()


	return

def subject_parser(folder_name, data_dir = r'./Data/Subject/'):
	"""
	Function that parses GenBank files introduced as Subject. They are fused 
	as a single msutifasta file
	"""
	#Format control
	
	for file in os.listdir(data_dir):
		with open(data_dir + file, 'r') as input_handle:
			for record in SeqIO.parse(input_handle, "genbank"):
				with open("./Data/" + folder_name + "/Subject/" + 
						  "Subject_db", 'a') as f: 
				#Dump to unique file
					for feature in record.features:
						if feature.type == "CDS":

							try: #CDS with lacking components are skipped 
								locus_tag = feature.qualifiers["locus_tag"][0]
								seq = feature.qualifiers["translation"][0]

								f.write(">" + locus_tag + "@" + record.id + "\n")
								f.write(seq + "\n\n")
							except:
								continue
				
				f.close()

	return