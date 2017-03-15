#!/usr/bin/python
import random
'''
Goal: to generate random fragments from an input sequence.
This program is a simulator which produces sequence reads when given the following inputs
Input: 1) a nucleotide sequence from which to take the fragments
       2) minimum fragment size
       3) maximum fragment size
       4) desired coverage
Output: a set of fragments and average coverage
'''
def simulateSequenceReads(file, minimum, maximum, coverage):
    # Step 0: Initialize
    infile = open(file, mode='r')
    infile.readline()
    seq1 = infile.read().strip().replace("\n","").replace("\r","")
    len1 = len(seq1)
    # check for bad input arguments
    if len1 < maximum or len1<minimum:
        raise ValueError('The minimum and maximum read lengths must be positive integers less than %d the length of the sequence' %len1)
    elif minimum>maximum:
        raise ValueError('The minimum read length %d cannot be greater than the maximum read length %d' %(minimum,maximum))

    minimum = minimum
    maximum = maximum
    requiredcoverage = coverage
    coverage =[0 for i in xrange(len1)]
    # ------------------------------------------------
    # Step 1: Define a function to check if the coverage is met everywhere
    # --------------
    def coverageMet(coverage,requeredCoverage):
        for i in coverage:
            if i < requeredCoverage:
                return False
        return True
    # ------------------------------------------------
    # Step 2: Generate a set of fragments for the input sequence
    # --------------
    fragments = []
    count = 0
    while not coverageMet(coverage, requiredcoverage):
        length = random.randint(minimum, maximum)
        start = random.randint(0, len1-length)
        end = start+length
        fragments.append(seq1[start:end])
        for i in xrange(start, end):
            coverage[i]+=1
        count+=1
    return fragments ,sum(coverage)/len(coverage)


if __name__ == '__main__':
    try:
        fragements,averageCoverage = simulateSequenceReads("CH08Klassevirusgenome.txt",5,8,1)
        print averageCoverage
    except ValueError as e:
        print e