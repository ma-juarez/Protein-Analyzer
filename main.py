import sys 

import arg_control_module as agc
import blast_module as bl
import domfinder_module as dm
import graphicator_module as gp
import help_module as hp
import muscle_module as ms
import parser_module as ps

#Control Argumentos
agc.arg_control(len(sys.argv))

#Ayuda
if sys.argv[1] == "-h" or sys.argv[1] == "-help":
	hp.help_message()
	exit()

graph = input("Desea realizar una representación gráfica de los resultados? "
			  "(Esto aumentará el tiempo de ejecución, llegando a tardar entre "
			  "5-10 minutos dependiendo de la computadora). [Y/n]")
#Creacion directorios y parser
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

#Graficacion
if graph.upper() == "Y":
	gp.tree_graph(sys.argv[1])
	gp.blast_graph(sys.argv[1])
	

print("\nEl programa ha terminado de ejecutar. Ya puede ver sus resultados")



