# import tools
import argparse

# add arguments
parser = argparse.ArgumentParser(description = "Open and read a GFF* file")
parser.add_argument("gff_File", help = "GFF File", type = str)
parser.add_argument("fasta_File", help = "FASTA File", type = str)

# parse 
args = parser.parse_args()

# print line by line
GFF_file = open(args.gff_file, "r")
GFF_Lines = GFF_file.readlines()
