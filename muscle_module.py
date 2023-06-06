import os

def tree_maker(folder_name):
	"""
	Function to perform Muscle alignment and local phylogenetic tree
	"""

	#Directory creation
	os.mkdir("./Results/" + folder_name + "/Muscle/Allignments")
	os.mkdir("./Results/" + folder_name + "/Muscle/Trees")

	for file in os.listdir("./Results/" + folder_name + "/Pre_muscle/"):

		allign = (" muscle -seqtype protein -in ./Results/" + folder_name 
				  + "/Pre_muscle/" + file + " -out ./Results/" + folder_name 
				  + "/Muscle/Allignments/" + file.replace('_premuscle', '') 
				  + "_allignment -quiet 2> /dev/null")

		try: 
			os.system(allign) #Local Muscle alignment
		except:
			print("No results for this sequence with the defined parameters" 
				  + file.replace('_premuscle', ''))

	for file in os.listdir("./Results/" + folder_name + "/Muscle/Allignments"):

		tree = (" muscle -maketree -in ./Results/" + folder_name + "/Muscle/" 
				"Allignments/" + file + " -out " + "./Results/" + folder_name 
			   + "/Muscle/Trees/" + file.replace('_allignment', '') 
			   + "_tree -cluster neighborjoining -quiet 2> /dev/null")
		try:
			os.system(tree) #Phylogenetic tree generation
		except: 
			print("No results for this sequence with the defined parameters" 
				  + file.replace('_premuscle', ''))

		
	return


