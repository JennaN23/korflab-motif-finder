# enumerate sequences based on their position weight matrix
# ie replace maybe a highish prob. of A or M
# decide using manhattan dist? 
import numpy as np
from collections import Counter
import sys 
import math

def psw(filename):
    # calc prob of each letter position by position
    # assign each position a letter
    with open(filename, 'r') as f:
        # read file into numpy array (rows: array of the sequence)
        lines = f.readlines()
        seq = [] 
        for line in lines:
            if not line.startswith('>') and line != "": 
                seq.append(np.array(list(line.strip())))
        seq = np.array(seq)
    print(seq)
    output_seq = ""
    for i in seq.T: # iterate down columns
        prob = Counter(i) # count freq of nuc. 
        # testing: using alphabet (ACGT)
        max_nuc = max(prob)
        # need to have rule for tiebreaker (currently by alphabetical order)
        if prob(max_nuc)/sum(prob.values()) < 0.5: # arbitrary?
            output_seq += 'N' # if prob. of max nucleotide < 50%, add N
        else:
            output_seq += max_nuc  # add nucleotide with max probability into the output sequence
    return output_seq

print(enumerate_seq(sys.argv[0]))

"""
motif-finder - given a collection of sequences, find the motifs in common (like MEME)
motif-positioner - given a sequence and a motif, find all of the matching positions
motif-scorer - given a sequence and motif, provide an aggregate score or probability
mult-motif-scorer - as above, but with a collection of sequences and motifs
motif-comparer - given two motifs, measure how similar they are to each other
motif-displayer - it might be convenient to display digitized motifs as more traditional PWMs
"""

def motif_positioner(sequences, motif):
    # finds all matching positions
    positions = []
    for seq in sequences.T: 
        for i in range(len(seq)-len(motif)+1):
            for j in range(len(motif)):
                if seq[i] != j:
                    break
            positions.append(i-len(motif))
    return positions

def get_CG_content(sequences):
    unique, counts = np.unique(sequences, return_counts=True)
    output = {}
    tot = sum(counts)
    for u, c in zip(unique, counts):
        output[u] = c/tot
    return output

def score_matrix(sequences):
    """
    score every letter:
    S(n) = log2[P(Cn)/Bn]
    Bn = background probability (use CG content or 0.25???)
    looks for prob of a certain letter in the seq being higher than that of the background prob   
    """
    Bn = get_CG_content(sequences)
    scores = []
    for seq in sequences.T: # iterate down columns
        freq = Counter(seq)
        tot = sum(freq.values())
        for key, value in freq.items(): # better way? broadcasting?
            freq[key] = value/tot # get prob.
        scores.append(freq) 
    for i in scores:
        for key, value in i.items():
            i[key] = math.log2(value/Bn[key])
    return scores

def motif_scorer(matrix, motif):
    pass

def motif-comparer(motif_a, motif_b):
    # measure how similar they are to each other
    pass

def display():
    # display scores underneath like in fastq

    pass 


# QUESTION:
# What is a motif score????
# need to figure out how to score ambiguities and gaps
# What to use for background probability (if using score equation)

# IDEAS:
# display scores instead of heights

# Enumerate: index each seq

# Define input

