# Created by ioluwayo on 2017-02-02.
"""
This python script does 2 main things.
1. It first counts the number of 'N's and 'A's in a DNA sequence
2. It then looks for the longest nucleotide repeat in a DNA sequence.
    e.g: If dna =  'AACCCGCTTAAAAC'.
    The longest nucleotide repeat = 'AAAA' at location 10. A repeats 4 times
"""
infile = open("gene.txt")
sequence =  infile.read().strip().replace("\n","")#remove new line character
numberOf_N = sequence.count('N')
numberOf_A = sequence.count('A')
print "Number of N:",numberOf_N
print "Number of A:",numberOf_A

# variables to assist in searching for longest nucleotide repeat in sequence.
count = 0
previous = ""
indexAfterLastNucleotide = 0
tempCounter = 1 # at the very least an index has a repeat length of 1.
for i in xrange(len(sequence)):
    if previous == sequence[i]: # if its the same nucleotide then increment the counter
        tempCounter += 1
        if i+1 == len(sequence) and count < tempCounter: # if at end of dna sequence and length is greater than biggest so far. Yay!
            count = tempCounter
            indexAfterLastNucleotide = len(sequence)
    else:# this gets executed only when the current nucleotide is different from the previous
        previous = sequence[i] # store current nucleotide to use for comparison in next iteration
        if count < tempCounter: # if the length of this repeat is greater than the biggest so far, then remember this.
            count = tempCounter
            indexAfterLastNucleotide = i
        tempCounter = 1 # re initialize temporary counter. At the very least, every index has a repeat length of 1.
longestRepeat = sequence[indexAfterLastNucleotide-count : indexAfterLastNucleotide]
startPosition = indexAfterLastNucleotide + 1- count
print "The longest repeat is at position",startPosition,"where",longestRepeat[0],"repeats",count,"times"