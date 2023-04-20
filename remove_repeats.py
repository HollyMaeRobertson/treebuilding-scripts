# script to remove repeated species data in the genes collected
import sys

if len(sys.argv) != 3:
    print("Usage: python3 remove_repeats.py SEQUENCE_FILE OUTFILE_NAME")
    sys.exit()

sequence_file = sys.argv[1]
outfile_final = open(sys.argv[2], "a")

species_seen = set()
repeated_species = []

# First pass: get the repeated species
with open(sequence_file, "r") as f:
    for line in f:
        line = line.strip()

        # look for repeats
        if line[0] == ">":
            if line in species_seen:
                if line not in repeated_species:
                    repeated_species.append(line)
            else: 
                species_seen.add(line)


# Next passes: getting the actual sequences.
correct_seqs = {}

for species in repeated_species:
    sequences = []
    longest_seq = None
    greatest_seq_len = 0
    seq = ''
    append_next = False

    with open(sequence_file, "r") as f:
        for line in f:
            line = line.strip()

            if line == species:
                if seq != '':
                    sequences.append(seq)
                    seq = ''
                append_next = True

            elif line[0] != ">" and append_next == True:
                seq += line.strip()
            
            elif line[0] == ">" and append_next == True:
                append_next = False
                sequences.append(seq)
                seq = ''

    if append_next == True:
        sequences.append(seq)
        seq = ''
        append_next = False

    for seq in sequences:
        total_len = len(seq)
        gaps = seq.count("-")
        seq_len = total_len - gaps
        if seq_len > greatest_seq_len:
            greatest_seq_len = seq_len
            longest_seq = seq

    correct_seqs[species] = longest_seq

append_next = True
with open(sequence_file,"r") as f:
    for line in f:
        line = line.strip()
        if line[0] != ">" and append_next == True:
            outfile_final.write(line + "\n")

        elif line[0] == ">" and line in correct_seqs.keys():
            append_next = False

        elif line[0] == ">":
            append_next = True
            outfile_final.write(line + "\n")
      
for species in correct_seqs.keys():
    outfile_final.write(species + "\n")
    outfile_final.write(correct_seqs[species] + "\n")

