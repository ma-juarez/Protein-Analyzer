# Protein-Analyzer

Final project for the Programming for bioinformatics course at the Universidad Politécnica de Madrid

This is a package dedicated to protein analysis, by usimg it you can obtain various types of information about the studied proteins. It also allows for the simultaneous study of multiple queries. Among the various results that we will obtain are: 

1. Blast of the queries against the various subjects.
2. Alignment in Muscle and construction of a phylogenetic tree.
3. Domain search in the different proteins based on the Prosite database.
4. Graphical representation of the Blast results and phylogenetic trees.

## Usage
To use this package as a standalone program, you should use the following command:  
`python3 main.py output-folder-name coverage-cutoff(optional) identity-cutoff(optional)`
  
The user will be asked if they want to generate graphical representations of the results or not. This can significantly increase the execution time, taking between 5-10 minutes.
  
It is necessary to have the external modules Matplotlib and Biopython installed, as well as locally having BlastP and Muscle.

## File Manegement
The package includes pre-defined folders for organizing both input and output files. 
### Input
The input files should be placed in the different subfolders of the **Data** folder following this structure:  
| Folder        |File       |
| ------------- |:-------------:|
| Query     |Multifasta or multiple fasta |
| Subject      | GenBanks   | 
| Domain_DB | prosite.dat   |  

It is crucial that the prosite.dat file is in Prosite format and has that exact name.

A folder with the name specified as the output folder will be generated, where the data used for analysis will be stored. This allows for changing the query and subject sequences in future analyses if desired.
 
### Output
Results will be stored in the **Results/Output_folder_name** folder, and the distribution of the files will be as follows:  
| Folder        |File       |
| ------------- |:-------------:|
| Blast     | Blast Results |
| Blast/Figures      | Blast Representations  | 
| Pre_Muscle | FASTA files for alignment |
| Muscle/Allignments | Muscle Alignments   |
| Muscle/Trees | Phylogenetic Trees   |
| Muscle/Trees_Figures | Drawn Phylogenetic Trees  |
| Domains | Domain Analysis |

## Results
### Blast
The results obtained from the Blast analysis are presented in a tabulated (TSV) file format, showing the following information:  
1. Query ID
2. Subject ID
3. Subject Seq
4. Coverage
5. identity
6. E-value  
  
By default, the values for the Coverage Cutoff and Identity Cutoff are set to 50 and 25, respectively, although these can be changed by the user. The E-value is set to 10<sup>-5</sup>.


The results obtained from the Blast analysis are presented in a tabulated (TSV) file format, showing the following information:

Query ID
Subject ID
Subject Seq
Coverage
Identity
E-value
By default, the values for the Coverage Cutoff and Identity Cutoff are set to 50 and 25, respectively, although these can be changed by the user. The E-value is set to 10<sup>-5</sup>.

Additionally, different representations of the Blast results will be obtained for each query. Here is an example image of the Blast representation:
![mrdA_figure](https://user-images.githubusercontent.com/67161655/85619606-d5e7a600-b662-11ea-8c29-fdec2fc8043e.png)

### Muscle
From Muscle, two types of files will be obtained: one file with the sequence alignment and another file with a phylogenetic tree. The phylogenetic tree can be further visualized using tools like iTOL for graphical representation.

Moreover a simple example image of the tree is represented using BioPython's Phylo:
![mrdA_tree](https://user-images.githubusercontent.com/67161655/85619625-dda74a80-b662-11ea-86f6-3e86d6def446.png)

### Domain Finder
An output file will be generated displaying the different domains present in each protein, along with a brief description, the pattern of the domains, and their positions.