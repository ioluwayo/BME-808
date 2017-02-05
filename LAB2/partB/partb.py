# Created by ioluwayo on 2017-02-01.
"""
This program translates a nucleotide sequence into its corresponding amino acid sequence.
I have written a more robust and interesting version of this same program in the past.
See https://github.com/ioluwayo/hackerank_challenge/tree/master/dna_mutation
"""
def translateToAminoAcid(nucleotideSequence):
    letters = ('G', 'A', 'C', 'T')
    nucleotides = []
    for a in letters:
        for b in letters:
            for c in letters:
                nucleotides.append(a + b + c)
    codons = {}
    acids = 'ggggeeddaaaavvvvrrsskknnttttmiiirrrrqqhhppppllllwxccxxyyssssllff'.upper()
    for i in range(64):
        codons[nucleotides[i]] = acids[i]
    aminoAcidSeq = ""
    for i in xrange(0,len(nucleotideSequence),3):
        aminoAcidSeq += codons[nucleotideSequence[i:i+3]]
    return aminoAcidSeq

if __name__ == '__main__':
    gene1 = "ATGGGGTCACAATCATCAAAATCTTTGGAACCAATTGTTGATACAAATGAAAGTTACAAGAGTGCCAGAAATATTTTGGAA" \
            "GATATTGGTAAAGGAATAAAAGATAAAGTAACAAAGGGTGCAGAAAAACGTGGTAAATCTTTGAAAGGAAATTTGTCAGAAGCAAAAT" \
            "TTTATCATGCGTACTCTAAGTATAGAACTGTCCCTGAAAGTCCATGTGATCTTAATTATGTATTTCATACTAATGTATGGCATGGTAACGCAGAAGA" \
            "TAGAAATCCTTGTCTCTTTAGTGATAAAAATCGTTTTTCAAACGAAAGCGAAGCAGAATGTTATAATAGTAAAATAACTGGTAATGAAGGTAAAATTGGAG" \
            "CATGTGCTCCATATAGAAGGAGAGAATTATGTGATTATAATTTGGAACATATAGATGTAAATAATGTGAAAAGTATTCATGATTTATTGGGGAATTTGTTAGT" \
            "TATGGCAAGGAGTGAAGGTGAATCTATTGTGAATAGTCATAAAAATACTGGCATGATAAACGTATGTGCTTCTCTTGCACGAAGTTTTGCTGATATAGG" \
            "CGATATTGTAAGAGGAAAGGATCTGTTTCTTGGTGATAATAAAGAAAGAAATAAAAAATTACAAGGGAATTTACAAAAAATTTTTAATACATTTCAAGAG" \
            "CATTATAAAGATCTTAAGAAAATTCCAATTGATGAGATTAGAGAATACTGGTGGGCACTTAATAGAAAAGAGGTATGGAAAGCCTTAACATGTTCTGGGTT" \
            "TAGGGTTTAG"
    print 'Part B: Task B'
    print 'Amino acid sequence for gene 1'
    aminioAcid = translateToAminoAcid(gene1)
    for i in xrange(0,len(aminioAcid),25):
        print aminioAcid[i:i+25]
