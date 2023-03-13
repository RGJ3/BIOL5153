Assignment 3 Markdown

1. rsync -r mt_genomes ronaldj@hpc-portal2.hpc.uark.edu:/storage/ronaldj

2. scp unknown.fa ronaldj@hpc-portal2.hpc.uark.edu:/storage/ronaldj/mt_genomes

3. Ran job script:

    #!/bin/bash

    #SBATCH --job-name=Assignment3
    #SBATCH --partition comp01
    #SBATCH --nodes=1
    #SBATCH --qos comp
    #SBATCH --tasks-per-node=1
    #SBATCH --time=1:00:00
    #SBATCH -o test_%j.out
    #SBATCH -e test_%j.err
    #SBATCH --mail-type=ALL
    #SBATCH --mail-user=ronaldj@uark.edu

    export OMP_NUM_THREADS=32

    module purge
    module load blast

    cd /storage/ronaldj/mt_genomes
    # job command here

    cat *.fasta > genomes.fas
    makeblastdb -in genomes.fas -dbtype nucl
    blastn -query unknown.fa -db genomes.fas > unknown.vs.genomes.blastn

4. rsync -av ronaldj@hpc-portal2.hpc.uark.edu:/storage/ronaldj/mt_genomes . 

Questions:

1. 00:00:03
2. Cucurbita 
3. It apears to be either Cucurbita or Carica as they match 99% of values