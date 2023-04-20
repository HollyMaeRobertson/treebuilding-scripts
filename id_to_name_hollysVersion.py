import sys
import seq
import os

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("python "+sys.argv[0]+" table infile outfile")
        sys.exit(0)
    tab = open(sys.argv[1],"r")
    idn = {}
    
    for i in tab:
        spls = i.strip().split("\t")
        idn[spls[3]] = spls[4]
    tab.close()
    
    outf = open(sys.argv[3],"w")
    for i in seq.read_fasta_file_iter(sys.argv[2]):
        
        # For when the name is wrongish
        if '.' in i.name:
            # take everything up to the '.' 
            key = i.name.split(".")[0]

            # just to be safe
            print(i.name)
            print("key: " + key)
        
        else:
            key = i.name

        i.name = idn[key].replace(" ","_")
        outf.write(i.get_fasta())
    outf.close()
   
