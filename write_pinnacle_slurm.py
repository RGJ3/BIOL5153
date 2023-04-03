#! /Users/RJ3/opt/anaconda3/bin/python3

# Import desired modules
import argparse

# Create argument parser object
parser = argparse.ArgumentParser(description="This script returns a SLURM file for jobs on the AHPCC cluster")

# add positional arguments
parser.add_argument("job_name", help = "The name of the SLURM job", type = str)

# Options for adding arguments
parser.add_argument("-q", "--queue", help = "Requested queue (comp01, comp06, comp72)", default = "comp72", type = str)
parser.add_argument("-n", "--num_nodes", help = "Number of HPC nodes to request", default = 1, type = int)
parser.add_argument("-p", "--processors", help = "Number of HPC processors to utilize", default = 1, type = int)
parser.add_argument("-w", "--walltime", help = "Length of the job", default = 1, type = int)

# Parse arguments
args = parser.parse_args()

print('#!/bin/bash')

print()

print('#SBATCH --job-name=' +args.job_name)
print('#SBATCH --partition ' + args.queue)
print('#SBATCH --nodes=' + str(args.num_nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=' + str(args.num_processors))
print('#SBATCH --time=' + str(args.walltime) + ':00:00')
print('#SBATCH -o test_%j.out')
print('#SBATCH -e test_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-ronaldj@uark.edu')

print()

print('module purge')

print()

print('cd $SLURM_SUBMIT_DIR')

print()

print('# job command here')
