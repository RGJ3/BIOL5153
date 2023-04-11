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
    for line in x:
        GFF_lines = line.readlines()


# strip the line breaks

for lines in GFF_lines:
    lines_stripped = lines.strip()

# use split() to isolate data in columns

for columns in lines_stripped:
    split_columns = columns.strip()

# print contents of specific columns in relation to eachother

length = int(split_columns[4]) - int(split_columns[3])
print(length)
