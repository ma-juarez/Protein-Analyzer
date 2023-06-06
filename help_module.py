
def help_message():
	"""
	Help menu function
	"""
	print("This is a package that allows to run an analysis over multipe " 
		  "proteins. A blastP will be carried out between query and subject sequences. "
		  "Furthermore, an alignment of the sequences will be performed, creating a "
		  "phylogenetic tree. SIn addition, proteins are also analysed for domains"
		  " based on a Prosite database\n")
	print("Usage: python3 main.py output-folder-name [Coverage-cutoff](Optional) "
		  "[Identity-Cutoff](Optional)\n")
	print("-Query files: Placed inside /Data/Query in FASTA or multiFASTA format ")
	print("-Subject files: Placed inside /Data/Subject in GenBank format")
	print("-Domain DataBase files: Placed inside /Data/Domain_DB as .dat format from Prosite")
	print("-Coverage Cutoff: Optional parameter that can be defined by the user. Default value 50")
	print("-Identity Cutoff: Optional parameter that can be defined by the user. Default value 25")
	print("-Graphication: Es una opción que se le preguntara al usuario. "
		  "This will increase the running time.")


	return
