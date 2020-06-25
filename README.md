# Protein-Analyzer

Este es un paquete dedicado al análisis de proteínas, mediante el cual se podrán obtener diversos tipos de información sobre las proteínas estudiadas. Además permite el estudio de múltiples querys al mismo tiempo. Entre los diversos resultados que obtendremos se encuentran:  

1. Blast de los querys frente a los diversos subjects
2. Alineamiento en Muscle y construcción de un árbol filogenético
3. Búsqueda de dominios en las distintas proteínas a partir de la base de datos de Prosite
2. Representación gráfica de los resultados de Blast y los árboles filogenéticos

## Usage
Para usar este paquete como un programa individual debe usarse:  
`python3 main.py output-folder-name coverage-cutoff(optional) identity-cutoff(optional)`
  
Se le preguntará al usuario si desea realizar la representación grafica de los resultados o no. Ya que esto puede incrementar considerablemente el tiempo de ejecución. Llegando a tardar entre 5-10 minutos.
  
Es necesario tener instalados los módulos externos Matplotlib y BioPython y a nivel local contar con BlastP y Muscle.

## File Manegement
Las carpetas en las que se organizarán tanto los archivos del input como los del output viene incluidas con el paquete.  
### Input
Los archivos input deben introducirse en las diferentes subcarpetas de la carpeta **Data** de la siguiente manera:  
| Carpeta        |Archivo       |
| ------------- |:-------------:|
| Query     |Multifasta o multiples fasta |
| Subject      | GenBanks   | 
| Domain_DB | prosite.dat   |  

Es muy importante que el archivo prosite.dat sea en formato Prosite y tenga ese nombre exactamente. 
 
### Output
Los resultados se almacenarán en la carpeta **Results/Output_folder_name** y la distribución de los mismos será:  
| Carpeta        |Archivo       |
| ------------- |:-------------:|
| Blast     |Resultados Blast |
| Blast/Figures      | Representación Blast   | 
| Pre_Muscle | Fastas para alineamiento  |
| Muscle/Allignments | Alineamientos de Muscle   |
| Muscle/Trees | Árboles Filogenéticos   |
| Muscle/Trees_Figures | Árboles Filogenéticos Dibujados  |
| Domains | Análisis de Dominios |

## Resultados
### Blast
Los resultados obtenidos mediante el análisis de Blast vienen dados en forma de archivo tabulado (tsv) y se muestra:  
1. Query ID
2. Subject ID
3. Subject Seq
4. Coverage
5. identity
6. Evalue  
Por defecto los valores de Coverage Cutoof y Identity Cutoff están definidos como 50 y 25 respectivamente, aunque estos se pueden cambiar por el usuario. El valor de evalue está definido como 10<sup>-5</sup>.  

También se obtendrán las distintas representaciones de los Blast para cada Query
![mrdA_figure](https://user-images.githubusercontent.com/67161655/85619606-d5e7a600-b662-11ea-8c29-fdec2fc8043e.png)

### Muscle
A partir de Muscle se obtendrán dos tipos de archivos. Un archivo con el anileamiento de las secuencias y otro con un árbol filogenético. El árbol podremos llevarlo posteriormente a herramientas como iTOL para poder visualizarlo gráficamente.  
También se presenta una imagen con el árbol representado mediante Phylo de BioPython

![mrdA_tree](https://user-images.githubusercontent.com/67161655/85619625-dda74a80-b662-11ea-86f6-3e86d6def446.png)

### Domain Finder
Se obtendrá un archivo en el que se mostrarán los distintos dominios presentes en cada proteína, una breve descripción, el patrón de los mismos y la posición en que aparecen.
