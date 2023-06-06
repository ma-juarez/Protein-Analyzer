import os
import re

from Bio.ExPASy import Prosite
from Bio import Seq,SeqIO
from Bio.Seq import Seq

def finder_filemaker(folder_name):
	"""
	Function to generate the files conatining complete sequences. This sequences 
	will be used to perform domain search
	"""
	os.mkdir("./Results/" + folder_name + "/Domains/tmp")
	#Query sequence addition
	for file in os.listdir(r'./Data/' + folder_name + '/Query/'):
		os.system("cp ./Data/" + folder_name + "/Query/" + file + " ./Results/" 
				  + folder_name + "/Domains/tmp/" + file + "_tmp")

	#Index method to avoid memory issues when parsing subject db
	fullprot_dict = SeqIO.index("./Data/" + folder_name + "/Subject/Subject_db",
							    "fasta")

	#Addition of sequences with same ID as Blast results
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
	Function that compares domains in database with the different prorteins. 
	This task is repeated for each alignment individualy. 
	"""
	
	#Results files header
	for file in os.listdir("./Results/" + folder_name + "/Domains/tmp"):
		with open("./Results/" + folder_name + "/Domains/" 
				  + file.replace("_tmp", "") + "_domains", 'a') as f:
			f.write("Domain Name\tDomain Accession\tDomain Description\t"
					"Domain Pattern\t Protein ID\tPosition\n")


		with open("./Results/" + folder_name + "/Domains/tmp/" + file, 
				  'r') as input_handle:
			#Protein iteration
			for protein in SeqIO.parse(input_handle, "fasta"):
				seq_re = str(protein.seq)

				handle = open("./Data/Domain_DB/prosite.dat", "r")
				domains = Prosite.parse(handle)

				#Iteration for each domain
				for domain in domains:
					pattern_pro = domain.pattern
					pattern_re = (pattern_pro.replace(".","").replace("x",".")
								 .replace("{","[^").replace("}","]").replace("(","{")
								 .replace(")","}").replace("<","^").replace(">","$")
								 .replace("-",""))
					
					#Pattern searching
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