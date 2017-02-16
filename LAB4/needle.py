# Created by ioluwayo on 2017-02-14.
#!/usr/bin/python
"""
This program determines the optimal global alignment of two downloaded_sequences.
Input: 2 sequences.
Output: best, global alignment of the 2 sequences.
"""
def calculatePercentIdentity(sequence1,sequence2):
    sequence1 = sequence1.rstrip('_')
    sequence2 = sequence2.rstrip('_')
    if len(sequence1)<len(sequence2):
        shorter =len(sequence1)
    else:
        shorter =len(sequence2)
    matches = 0
    gaps =0
    for i in xrange(shorter):
        if sequence1[i] == sequence2[i]:
            matches+=1
        elif sequence1[i] == '_' or sequence2[i]== '_':
            gaps+=1

    percentIdentity = matches*100.0/shorter
    percentgaps =  gaps *100.0/shorter
    print percentIdentity
    print percentgaps
def buildAlignment(seq1, seq2, direction):
    l1 = 0
    l2 = 0
    align1=""
    align2 =""
    for i in xrange(len(direction)):
        if direction[i] == "D":
            if l1 < len(seq1):
                align1 += seq1[l1]
            if l2 < len(seq2):
                align2 += seq2[l2]
            if l1>=len(seq1):
                align1 +="_"
            if l2 >=len(seq2):
                align2+="_"
            l1+=1
            l2+=1
        elif direction[i] == "V":
            align1+="_"
            if l2 < len(seq2):
                align2+=seq2[l2]
            l2+=1
        else:
            if l1<len(seq1):
                align1+=seq1[l1]
            align2+="_"
            l1+=1
    print "\n-----OPTIMAL GLOGAL ALIGNMENT-----"
    print "SEQ 1:",align1
    print "SEQ 2:",align2



def buildDirectionalString(matrix,gapScore):
    currentRow = len(matrix)-1
    currentCol = len(matrix[0])-1
    direction = ""
    # start from the end and build a string with either D, H, V based on matrix values
    while currentRow or currentCol:
        if currentRow == 0:
            # then we have a horizontal gap. use horizontal only. gaps for the vertical sequence
            direction = "H"+direction
            currentCol -= 1
        elif currentCol == 0:
            # then we us the vertical sequence only.. gaps for the horizontal sequence
            direction = "V"+direction
            currentRow -= 1
        elif matrix[currentRow-1][currentCol]+gapScore == matrix[currentRow][currentCol]:
            #then we use the vertical sequence...gap for the horizontal sequence
            direction = "V"+direction
            currentRow -= 1
        elif matrix[currentRow][currentCol-1]+gapScore == matrix[currentRow][currentCol]:
            # then we use the horizontal sequence.. gap for the vertical sequence
            direction = "H"+direction
            currentCol -=1
        else:
            # for sure its from the diagonal
            direction = "D"+ direction
            currentRow -= 1
            currentCol -= 1
    return direction


def find_global_alignment(pathToSequence1, patheTosequence2):
    infile1 = open(pathToSequence1)
    infile2 = open(patheTosequence2)
    sequence1 = ""
    sequence2 = ""
    fasta1 = infile1.readline()
    fastat2 = infile2.readline()
    for line in infile1:
        sequence1 += line.replace("\n", "").strip()
    for line in infile2:
        sequence2 += line.replace("\n", "").strip()
    lengthOfSeq1 = len(sequence1)
    lengthOfSeq2 = len(sequence2)
    matrix = [[0 for x in xrange(lengthOfSeq2 + 1)] for y in xrange(lengthOfSeq1 + 1)]
    # print matrix
    gap = -1
    mismatch = 0
    match = 1
    # now we initialize 1st row with 0.-1.-2.-3....-n
    for i in xrange(lengthOfSeq1 + 1):
        matrix[i][0] = i * -1  # columns of row 0
    for i in xrange(lengthOfSeq2 + 1):
        matrix[0][i] = i * -1  # rows of column 0
    # now we fill the matrix boxes with the highest of the value based on scoring rule
    for i in xrange(1, lengthOfSeq1 + 1):  # for each element in the row
        for j in xrange(1, lengthOfSeq2 + 1):  # for each element in the column
            if sequence1[i - 1] == sequence2[j - 1]:
                # there is a match
                matchScore = match + matrix[i - 1][j - 1]
            else:
                # no match
                matchScore = mismatch + matrix[i - 1][j - 1]
            # always have to calculate the gap scores.
            hGapScore = gap + matrix[i - 1][j]  # horizontal gap
            vGapScore = gap + matrix[i][j - 1]  # vertical gap
            matrix[i][j] = max(matchScore, hGapScore, vGapScore)
    # now we've got the matrix filled up. matrix[N][M] has the final score:
    direction = buildDirectionalString(matrix, gapScore = gap)
    buildAlignment(sequence1,sequence2,direction)
    print "Score = ", matrix[-1][-1]
    percentIdentity = 100.0* direction.count("D")/len(direction)
    percentGap = 100.0 *(len(direction)-direction.count("D"))/len(direction)
    print "Percent identity =",percentIdentity,"%"
    print "Percent Gap =",percentGap,"%"
    print "\n"

if __name__ == '__main__':
    import sys
    find_global_alignment(sys.argv[1], sys.argv[2])
    calculatePercentIdentity("ee_a_a","eeaae")