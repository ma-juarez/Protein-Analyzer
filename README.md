# Protein-Domain-Finder

Este es un paquete dedicado al análisis de proteínas, mediante el cual se podrán obtener diversos tipos de información sobre las proteínas estudiadas. Además permite el estudio de múltiples querys al mismo tiempo. Entre los diversos resultados que obtendremos se encuentran:  

1. Blast de los querys frente a los diversos subjects
2. Representación gráfica de estos resultados
3. Alineamiento en Muscle y construcción de un árbol filogenético
4. Búsqueda de dominios en las distintas proteínas a partir de la base de datos de Prosite

## Usage
Para usar este paquete como un programa individual debe usarse:  
`python3 main.py output-folder-name coverage-cutoff(optional) identity-cutoff(optional)`

## File Manegement
Las carpetas en las que se organizarán tanto los archivos del input como los del output viene incluidas con el paquete.  
### Input
Los archivos input deben introducirse en las diferentes subcarpetas de la carpeta **Data** de la siguiente manera:  
| Carpeta        |Archivo       |
| ------------- |:-------------:|
| Query     |Multifasta o multiples fasta |
| Subject      | GenBanks   | 
| Domain_DB | Prosite.dat   |  
 
### Output
Los resultados se almacenarán en la carpeta **Results/Output_folder_name** y la distribución de los mismos será:  
| Carpeta        |Archivo       |
| ------------- |:-------------:|
| Blast     |Resultados Blast |
| Blast/Figures      | Representación Blast   | 
| Pre_Muscle | Fastas para alineamiento  |
| Muscle/Allignments | Alineamientos de Muscle   |
| Muscle/Trees | Árboles Filogenéticos   |
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

### Muscle
A partir de Muscle se obtendrán dos tipos de archivos. Un archivo con el anileamiento de las secuencias y otro con un árbol filogenético. El árbol podremos llevarlo posteriormente a herramientas como iTOL para poder visualizarlo gráficamente.  

### Domain Finder
Se obtendrá un archivo en el que se mostrarán los distintos dominios presentes en cada proteína, una breve descripción, el patrón de los mismos y la posición en que aparecen.
