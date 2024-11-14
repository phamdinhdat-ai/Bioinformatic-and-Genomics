from genome_toolkit import genomeToolkit
from utils import colour_seq


with open("rosalind_dna.txt", 'r') as f:
    dna_seq = f.read().strip()
tool = genomeToolkit()
most_kmer = tool.find_most_frequent_kmers(sequence=dna_seq, k_len=5)
print("Most of K Sequence in DNA :", most_kmer)
print("Sequence DNA: ", colour_seq(dna_seq))
for kmer in most_kmer:
    print("Kmer sequence: ", colour_seq(kmer))
    print("Count values: ", tool.count_kmer(dna_seq, kmer=kmer))