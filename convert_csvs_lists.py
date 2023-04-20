# A script to take an info.csv and print out a single line with all the species named in it, underscore-separated

import sys

if len(sys.argv) != 2:
    print("Usage: python3 convert_csvs_lists.py FILE_TO_CONVERT")
    sys.exit()

# initialise
input_file = open(sys.argv[1], "r")
index = 0
species_list = []

# read the file
for line in input_file:
    if index != 0:
        # take the first bit before the comma and put it in a list 
        name = line.split(",")[0]
        
        # take the name and replace the space with an underscor
        name = name.replace(" ", "_")
        species_list.append(name)

    index += 1

species_string = ",".join(species_list)
print(species_string)

