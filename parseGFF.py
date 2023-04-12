# import tools

import argparse

# set description

parser = argparse.ArgumentParser(description = "This script parses a GFF* file")

# add arguments

parser.add_argument("gff", help = "Name of the GFF file to parse", type = str)
parser.add_argument("fasta", help = "Name of the FASTA file to parse", type = str)

# parse arguments

args = parser.parse_args()

# read line by line
# GFF_file = open(args.gff_file, "r")
# GFF_Lines = GFF_file.readlines()

# use a for loop to open and read the GFF file

with open(args.gff) as x:
    
    # loop over all the lines in the file
    for line in x:

        # skip blank lines
        if not line.strip():
            continue
            
        # else it's not a blank line
        else:
            line = line.strip()

            # split line on the tab character
            columns = line.split('\t')

            # give variable names to the columns
            organism     = columns[0]
            source       = columns[1]
            feature_type = columns[2]
            start        = int(columns[3])
            end          = int(columns[4])
            length       = columns[5]
            strand       = columns[6]
            attributes   = columns[8]


            # add the length to column 5
            columns[5] = str(end - start + 1)

            # join columns back into a tab-separated line
            new_line = "/t".join(columns)
            print(new_line)