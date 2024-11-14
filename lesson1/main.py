from DNAToolkit  import * 
import random
dna_seq = "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"

dna_seq_invalid = "CCTGCGGAAGdATCGGCACTAsGAATAGCCsAGAACCGTTTCTC"


randnDNAstr = ''.join(random.choice(nucleotides) for nuc in range(100))


print("="*100)
print("check valid sequece: ", dna_seq)
print("Result: ", checkValidSeq(dna_seq=dna_seq))
print("="*100)

print("check Invalid Sequence: ", dna_seq_invalid)
print("Results: ", checkValidSeq(dna_seq_invalid))
print("="*100)

print("check Random Sequence: ", randnDNAstr)
print("Results: ", checkValidSeq(randnDNAstr))
print("="*100)


print("count Random Sequence: ", randnDNAstr)
print("Results: ", countDNASeq(randnDNAstr))
print("="*100)


print("Original DNA: ", randnDNAstr)
print("Transcript to RNA")
print("RNA: ", transcription(randnDNAstr))
print("="*100)


print(f"5' {randnDNAstr}    '3")
print(f"   {''.join(['|' for c in range(len(randnDNAstr))])}")
print(f"3' {reverseDNA(randnDNAstr)}    '5")

print("="*100)



print("Coloured DNA: ", colour_seq(randnDNAstr))
print("Transcript to RNA")
print("Coloured RNA: ", colour_seq(transcription(randnDNAstr)))
print("="*100)