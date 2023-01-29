import gzip
import sys

# motif-positioner
# given a sequence and a motif, find all of the matching positions

# input: FASTA??

# take into account lowercase/ambiguity codes?

# FASTA

motif = sys.argv[2]
ml    = len(motif)

with open(sys.argv[1], "rt") as fp:
	for line in fp.readlines():
		if line[0] == ">": 
			print(line.lstrip(">"), end='')
			continue
		sl = len(line)
		for i in range(sl - ml + 1):
			if line[i:i + ml] == motif: print(i + 1)


"""
# as function

def motif_positioner(seq, motif):
	ml = len(motif)
	for i in range(len(seq) - len(motif) + 1):
		if line[i:i + ml] == motif: print(i + 1)
		
m = sys.argv[2]
		
with open(sys.argv[1], "rt") as fp:
	for line in fp.readlines():
		if line[0] == ">":
			#print(line.lstrip(">"), end="")
			continue
		print(motif-positioner(line, m))
"""

"""
# CLI

seq   = sys.argv[1]
motif = sys.argv[2]
ml    = len(motif)

for i in range(len(seq) - ml + 1):
	if seq[i:i + ml] == motif: print(i + 1)
"""

