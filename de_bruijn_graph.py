import itertools

with open("input.txt", "r") as file:
	k = int(file.readline())
	sequence = file.readline().strip()

k = k - 1
kmers = [sequence[x : x + k] for x in range(len(sequence) - k + 1)]
kmers = sorted(list(set(kmers)))
output = open("output.txt", "w")

for kmer1 in kmers:
	index = kmers.index(kmer1)
	overlap = []
	for kmer2 in kmers[:index] + kmers[index + 1:]:
		if kmer1[1:] == kmer2[:-1] and kmer2 not in overlap: 
			overlap.append(kmer2)
	if len(overlap) > 0:
		output.write(kmer1 + ' -> ' + ','.join(overlap) + '\n')
