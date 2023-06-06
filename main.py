import sys 

import arg_control_module as agc
import blast_module as bl
import domfinder_module as dm
import graphicator_module as gp
import help_module as hp
import muscle_module as ms
import parser_module as ps

#Arg control
agc.arg_control(len(sys.argv))

#Help
if sys.argv[1] == "-h" or sys.argv[1] == "-help":
	hp.help_message()
	exit()

graph = input("Would to like to graph the results?"
			  "(This will increase running time, taking around "
			  "5-10 minutes depending on your computer). [Y/n]")
#Directory creation and parser
ps.dir_maker(sys.argv[1])
ps.query_parser(sys.argv[1])
ps.subject_parser(sys.argv[1])

#Blast
bl.blast(sys.argv[1])
try:
	bl.blast_filter(sys.argv[1], sys.argv[2], sys.argv[3])
except:
	bl.blast_filter(sys.argv[1])

#Muscle
ms.tree_maker(sys.argv[1])

#Domain finder
dm.finder_filemaker(sys.argv[1])
dm.finder(sys.argv[1])

#Graphs
if graph.upper() == "Y":
	gp.tree_graph(sys.argv[1])
	gp.blast_graph(sys.argv[1])
	

print("\nThe program finished. You can now check your results")



