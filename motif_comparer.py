import sys

# motif-comparer
# given 2 motifs, measure how similar they are to each other 

# take into account lowercase/ambiguity codes?

m1    = sys.argv[1]
m2    = sys.argv[2]
min   = len(m1)
max   = len(m2)
score = 0

if min > len(m2):
	min = len(m2)
	max = len(m1)

for i in range(min):
	if m1[i] == m2[i]: score += 1
print(score/max)
