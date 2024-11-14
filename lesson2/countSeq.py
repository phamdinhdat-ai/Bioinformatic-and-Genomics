
with open('rosalind_dna.txt', 'r') as f:
    dna_sq = f.readline().strip()
    

    
def countDNASeq(dna_seq):
    tempDict = {"A":0, "C":0, "G":0, "T":0}
    for nuc in dna_seq:
        tempDict[nuc] += 1
    return ' '.join([str(val) for key, val in tempDict.items()])

print("Count DNA Sequence: ", dna_sq)
print("Result: ", countDNASeq(dna_seq=dna_sq))