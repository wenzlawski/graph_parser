#!/bin/bash --login
#$ -cwd

#$ -l v100=2
#$ -pe smp.pe 8

export OMP_NUM_THREADS=$NSLOTS

# load modules
module load apps/binapps/pytorch/1.11.0-39-gpu-cu113
module load tools/env/proxy2

source activate mlflow

./examples/multitask_am/setup_all.sh