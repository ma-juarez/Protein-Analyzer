import os

import matplotlib.pyplot as plt

from Bio import Phylo
from Bio import Seq,SeqIO
from Bio.Seq import Seq

def blast_graph(folder_name):
	"""
	Funcion que genera una representacion grafica de los resultados de Blast,
	en forma de alinemaiento. Mostrando las regiones coincidentes y las que no

	Function to create a graphical representation of the Blast results as an alignment. 
	Matching and non matching regions are formated differently. 
	"""

	counter_seq = 1 #Protein position

	os.mkdir("./Results/" + folder_name + "/Blast/Figures")

	for file in os.listdir("./Results/" + folder_name + "/Muscle/Allignments/"):
		
		plt.figure(figsize = (25,15))
		plt.style.use("ggplot") #Plot style

		with open("./Results/" + folder_name + "/Muscle/Allignments/" + file,
				  'r') as input_handle:
			for record in SeqIO.parse(input_handle, "fasta"):
				seq = str(record.seq)
				counter_aa = 0 #Amino acid position
				

				for char in seq:
					if char.isalpha(): #If match
						counter_aa += 1
						plt.scatter(counter_aa, counter_seq, s = 10, marker = "s",
								    color = "Red")


					else: #Not match
						counter_aa += 1
						plt.scatter(counter_aa, counter_seq, s = 10, marker = 1, 
									color = "Blue")

				plt.annotate(record.id, (counter_aa, counter_seq)) #Protein name
				counter_seq += 1

		plt.grid(False)
		plt.title("Alineamiento Blast " + file.replace("_allignment", ""))
		plt.savefig("./Results/" + folder_name + "/Blast/Figures/" 
					+ file.replace("_allignment", "") + "_figure.png") 
		#Plot saving to folder

	return

def tree_graph(folder_name):
	"""
		Funtion that drwas the phylogenetic trees and saves the, as a .png image
	"""

	os.mkdir("./Results/" + folder_name + "/Muscle/Trees_Figures")

	for file in os.listdir("./Results/" + folder_name + "/Muscle/Trees/"):
		tree = Phylo.read("./Results/" + folder_name + "/Muscle/Trees/"
						  + file, 'newick')
		fig = plt.figure(figsize = (25,15), dpi = 100)
		axes = fig.add_subplot(1, 1, 1)
		tree.ladderize() #Branch manipulation to make tree pretier
		Phylo.draw(tree, axes = axes, do_show = False)
		plt.savefig("./Results/" + folder_name + "/Muscle/Trees_Figures/"
					+ file)

	return

		
