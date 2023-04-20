# A script to check check if the species in one file fasta are not in another

import sys

if len(sys.argv) != 3:
    print("Usage: python3 check_list.py REF_FILE CHECK_FILE")
    sys.exit()

# initialise
ref_file = open(sys.argv[1], "r")
check_file = open(sys.argv[2], "r")
species_list = []

# Get a reference list
for line in ref_file:
    line = line.strip()
    names = line.split(',')
    species_list.extend(names)


# Check the file for items not in the list
for line in check_file:
    if line[0] == ">":
        line = line.strip()
        line = line[1:]
        if line not in species_list:
            print(line)

