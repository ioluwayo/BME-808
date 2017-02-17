# Created by ioluwayo on 2017-02-16.
#!/usr/bin/python

def main(pathToseq, start, end, pathToOutputFile):
    """
    This function accepts the relative path to a sequence (FASTA format), start and end indexes and an output file path.
    It copies the specified region [start-end] inclusive of the sequence and writes it in the output file.
    Start = 1 refers to the first nucleotide in the sequence. Not 0.
    :param pathToseq:
    :param start:
    :param end:
    :param pathToOutputFile:
    :return:
    """
    infile = open(pathToseq)
    outfile = open(pathToOutputFile, 'w')
    fasta = infile.readline().replace("\n","")
    sequence =""
    for line in infile:
        sequence+=line.replace("\n","")
    infile.close()
    outfile.write("Region "+start +" - "+ end + " of "+fasta)

    outfile.write("\n"+sequence[int(start): int(end)])
    outfile.close()
if __name__ == '__main__':
    import sys
    main(sys.argv[1],sys.argv[2],sys.argv[3], sys.argv[4])