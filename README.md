# BME-808
This repository contains python code for the optional parts of labs in my Computations in Genetic Engineering (BME808) course at Ryerson University.
### Lab 2 ###
In part A of lab 2, The task is to write a python script that calculates the frequency of nuceleotide on a string.
In part B of lab 2, The task is to write a python script that translates a nucleotide sequence into its corresponding amino acid sequence.
see [DNA mutation](https://github.com/ioluwayo/hackerank_challenge/tree/master/dna_mutation) for a more robust implementation
### Lab 3 ###
In lab 3 the task is to write a python program that does 2 things.
1. it first counts the number of 'N's and 'A's in a DNA sequence.
2. It then looks for the longest nucleotide repeat in a DNA sequence.
e.g: If dna =  'AACCCGCTTAAAAC'.
    The longest nucleotide repeat = 'AAAA' at location 10. 'A' repeats 4 times

### Lab 4 ###
Lab 4 involves the implementation of a global alignment algorithm known as the Needleman wunsch algortithm.
It uses dynamic programing to find the optimal global alignment between to DNA sequences. see https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
See [program](https://github.com/ioluwayo/BME-808/blob/master/LAB4/needle.py) for my implementation of the algorithm which uses path finding to achive the alignement between the sequences.

To use this program, you can import it as a module and then use it like
```
from needle import find_global_alignment
alignment1, alignment2, score, percentIdentity, percentGaps = find_global_alignment(pathToSeq1, pathToseq2)
```
or through the command line. See images below.
 ![Alt text](images/lab4/image1.png?raw=true "Global alignment")
 ![Alt text](images/lab4/image2.png?raw=true "Basis of algorithm")
 ![Alt text](images/lab4/image3.png?raw=true "Path finding")
 ![Alt text](images/lab4/screenshot1.png?raw=true "Sample run")
 ![Alt text](images/lab4/screenshot2.png?raw=true "Sample run")

