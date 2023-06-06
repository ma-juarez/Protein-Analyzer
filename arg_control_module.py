import os

def arg_control(num_arg):
	"""
	Function to control that the number of arguments is correct and
	that input files are the correct type
	"""

	if num_arg < 2:
		print("The number of arguments introduced does not match the expected."
			  " Revise the arguments.")
		print("For help please use the command -h or -help")
		exit()
	elif len(os.listdir("./Data/Query")) == 0:
		print("No file was introduced as Query. Please verify that"
			  " the multifasta or multiple FASTA files were introduced "
			  "inside the folder ./Data/Query ")
		print("For help please use the command -h or -help")
		exit()
	elif len(os.listdir("./Data/Subject")) == 0:
		print("No file introduced as Subject. Verify that"
			  " the GenBank file is located inside the folder ./Data/Subject")
		print("For help please use the command -h or -help")
		exit()
	elif len(os.listdir("./Data/Domain_DB")) == 0:
		print("No file inputed as Domain_DB. Verify that "
			  "the file .dat from prosite is located inside the folder ./Data/Domain_DB")
		print("For help please use the command -h or -help")
		exit()
