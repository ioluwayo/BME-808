# Created by ioluwayo on 2017-01-26.
#There are 336 genes on  Chromosome 6 of Plasmodium falciparum.
import re
def calculateNucleotideFrequency (occurrences, total):
    return float(occurrences)/float(total)

def countOccurrence (nucleotide, sequence):
    return (sequence.count(nucleotide))


if __name__ == '__main__':

    #Task B
    infile = open('sequence.txt')
    sequence = {'fasta':infile.readline(),'seq':infile.read().strip().replace('\n',"")}
    print "Lab 1 Part A:"
    print sequence['fasta']
    sequenceLength = len(sequence['seq'])
    subSeq = ["A","C","G","T","AT","GC"]
    print "Task B. Frequencies of",subSeq
    for i in subSeq:
        print i +": %.4f" %calculateNucleotideFrequency(countOccurrence(i, sequence['seq']),sequenceLength)
    infile.close()

    #Task C
    infile = open("gene_feautures.txt")
    geneSeq = ""
    for line in infile:
        if line[0] == ">":
            pass
        else:
            geneSeq += line.strip()
    geneSeqLength = len(geneSeq)
    subSeq = ["A","C", "T", "G","AT"]
    print "Task C Frequencies of", subSeq
    for i in subSeq:
        print i +": %.4f" %calculateNucleotideFrequency(countOccurrence(i, geneSeq),geneSeqLength)
    infile.close()