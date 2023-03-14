#!/bin/bash --login
#$ -cwd

#$ -l v100=2
#$ -pe smp.pe 8

# load modules
module load apps/binapps/pytorch/1.11.0-39-gpu-cu113

export OMP_NUM_THREADS=$NSLOTS

# initialise the environment
./examples/multitask_am/install.sh
./examples/multitask_am/setup_all.sh
./examples/multitask_am/mt_all/aaec_essay.sh