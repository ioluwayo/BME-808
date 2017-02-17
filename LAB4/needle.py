# Created by ioluwayo on 2017-02-14.
#!/usr/bin/python
"""
This program determines the optimal global alignment of two sequences using the Nedleman-Wunsh algorithm. See Read me.
Input: 2 sequences.
Output: best, global alignment of the 2 sequences.
"""
import sys
def calculatePercentIdentity(sequence1,sequence2):
    """
    This function accepts 2 sequences and calculates the percent identity and percent gaps.

    Percent identity is calculated by multiplying the number of matches in the pair by 100 and
    dividing by the length of the aligned region, including gaps.
    Identity scoring only counts perfect matches, and does not consider the degree of similarity nucleotides.
    Note that only internal gaps are included in the length, not gaps at the sequence ends.

    :param sequence1:
    :param sequence2:
    :return:
    """
    sequence1 = sequence1.rstrip("_")
    sequence2 = sequence2.rstrip("_")
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
    return percentIdentity,percentgaps

def buildAlignment(seq1, seq2, direction):
    """
    This function uses a directional string of the form DHVDD... (D = Diagonal, H = horizontal, and V = vertical edge)
    to create an alignment on 2 sequences
    e.g     SEQ 1: ACT__GGTCAATCG
            SEQ 2: ACTTCAATCGGT__
    :param seq1:
    :param seq2:
    :param direction:
    :return:
    """
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
        elif direction[i] == "H":
            if l2 < len(seq2):
                align2+=seq2[l2]
            if l1>=0:
                align1 += "_"
            l2+=1
        else:
            if l1< len(seq1):
                align1+=seq1[l1]
            if l1>=0:
                align2+="_"
            l1+=1

    return align1,align2

def buildDirectionalString(matrix,gapScore):
    """
    This function uses a simple path finding algorithm.
    It builds a directional string based on the values in a matrix.
    It traces the path from the last cell i.e matrix[-1][-1] to the first cell i.e matrix[-1][-1] following
    the edges that led to the optimal score in each cell.
    :param matrix:
    :param gapScore:
    :return:
    """
    currentRow = len(matrix)-1
    currentCol = len(matrix[0])-1
    direction = ""
    # start from the end and build a string with either D, H, V based on edges leading optimal score
    while currentRow or currentCol:#
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


def find_global_alignment(pathToSequence1, patheTosequence2, match = 1, mismatch = 0, gap = -1):
    """
    This function accepts the relative path to 2 files containing DNA sequences(FASTA format) as input and find the
     global alignment of the sequences in the files. It prints out the score, alignment, percent identity & percent gaps

    The scoring function can also be specified by passing the match, mismatch and gap scores to the function.

    :param pathToSequence1:
    :param patheTosequence2:
    :param match: (optional) default = 1
    :param mismatch: (optional) default = 0
    :param gap: (optional) default = -1
    :return: alignment1, alignment2, score, percentIdentity, percentGap
    """
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
    matrix = [[0 for x in xrange(lengthOfSeq2 + 1)] for y in xrange(lengthOfSeq1 + 1)] # initialize matrix with zeros

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
    score = matrix[-1][-1] # the global alignment score is the value of the last cell of the matrix
    direction = buildDirectionalString(matrix, gapScore = gap)
    alignment1, alignment2 = buildAlignment(sequence1,sequence2,direction)
    percentIdentity, percentGap = calculatePercentIdentity(alignment1, alignment2)
    return alignment1, alignment2, score, percentIdentity, percentGap

if __name__ == '__main__':
    alignment1, alignment2, score, percentIdentity, percentGap = find_global_alignment(sys.argv[1], sys.argv[2])
    print "-----OPTIMAL GLOBAL ALIGNMENT-----"
    print "Score = ", score
    print "SEQ 1:", alignment1
    print "SEQ 2:", alignment2
    print "Only aligned region is used to calculate percentage."
    print "Percent identity =", percentIdentity, "%"
    print "Percent Gap =", percentGap, "%"
    print "\n"