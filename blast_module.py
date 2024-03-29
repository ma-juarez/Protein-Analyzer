import os 

def blast(folder_name):
	"""
	Function to run a blast over the FASTA generated in parser_module
	"""
	
	for file in os.listdir(r'./Data/' + folder_name + '/Query/'):

		cmd = (" blastp -query ./Data/" + folder_name + "/Query/" + file  
			   + " -subject ./Data/" + folder_name + "/Subject/Subject_db "
			   "-out ./Results/" + folder_name + "/Blast/" + file + "_blast_tmp "
			   "-evalue 0.00001 -outfmt '6 qseqid sseqid sseq qcovs pident evalue '")

		os.system(cmd) #Local blast
	
	return 

def blast_filter(folder_name, cov_cutoff = 50, ident_cutoff = 25):
	"""
	Funcion para filtrar los datos brutos del Blast en funcion de coverage y 
	Identity. Obtencion de resultado final de Blast y de archivo fasta que es 
	input para Muscle

	Function to filter the raw Blast data based on coverage and 
	identity. Final Blast result generation and a FASTA file 
	which serves as input for Muscle will be generated.
	"""

	#Add query sequence to pre-muscle
	for file in os.listdir(r'./Data/' + folder_name + '/Query/'):
		os.system("cp ./Data/" + folder_name + "/Query/" + file + " ./Results/" 
				  + folder_name + "/Pre_muscle/" + file + "_premuscle")

	
	for file in os.listdir(r"./Results/" + folder_name + "/Blast/"):

		#AWK filters

		#Data Retention
		filt_blast = (" awk -v cov=" + str(cov_cutoff) + " -v ident=" 
					  + str(ident_cutoff) + " '{if ($4>=cov && $5>=ident) print" 
					  "$0\"\\n\"}' ./Results/" + folder_name + "/Blast/"+ file 
					  + " >> ./Results/" + folder_name + "/Blast/" 
					  + file.replace('_blast_tmp', '') + "_blast")
		
		with open("./Results/" + folder_name + "/Blast/" 
				  + file.replace('_blast_tmp', '') + "_blast", 'w+') as f:
			f.write("Query_seq Subject_seq Subject_seq Coverage Identity Evalue \n")
			f.close()
			
		os.system(filt_blast) #Final Blast Results

		#Name and sequence retention
		filt_allign = (" awk -v cov=" + str(cov_cutoff) + " -v ident=" 
					  + str(ident_cutoff) + " '{if ($4>=cov && $5>=ident) print" 
					  " \"\\n\"\">\"$2\"\\n\"$3}' ./Results/" + folder_name + "/Blast/" 
					  + file + " >> ./Results/" + folder_name + "/Pre_muscle/" 
					  + file.replace('_blast_tmp', '') + "_premuscle")

		os.system(filt_allign)#Pre-muscle file

		#Temporal Blast Erasing
		os.remove("./Results/" + folder_name + "/Blast/" + file)

	return







