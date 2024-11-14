
#import library 
import collections
nucleotides = ['A', 'T', 'G', 'C']

reverseCompliment = {"A":"T", "C":"G", "G":"C", "T":"A"}

def checkValidSeq(dna_seq):
    tmp = dna_seq.upper()
    for nuc in tmp:
        if nuc not in nucleotides:
            return False
    return tmp


def countDNASeq(dna_seq):
    tempDict = {"A":0, "C":0, "G":0, "T":0}
    for nuc in dna_seq:
        tempDict[nuc] += 1
    return tempDict
    # return collections.Counter(dna_seq)
    
    
    
def transcription(dna_seq):
    return dna_seq.replace('T', 'U')


def reverseDNA(dna_seq):
    out_seq = ''
    for nuc in dna_seq:
        out_seq+=reverseCompliment[nuc]
    return out_seq[: : -1 ]


def colour_seq(dna_seq):
    bcolours = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
    }
    tmpStr = ""
    for nuc in dna_seq:
        if nuc in bcolours:
            tmpStr += bcolours[nuc] + nuc
        else: 
            tmpStr += bcolours['reset'] + nuc
    return tmpStr + '\033[0;0m'