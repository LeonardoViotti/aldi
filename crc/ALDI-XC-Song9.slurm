#!/bin/bash
#SBATCH --job-name=aldi-XC-s9
#SBATCH --output=out/aldi-XC-s9.out
#SBATCH --time=3-00:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=10
#SBATCH --cpus-per-task=1
#SBATCH --cluster=gpu
#SBATCH --partition=a100
#SBATCH --gres=gpu:1
#SBATCH --mem=100G

module purge
module load pytorch/2.0.1_cuda11.8 gcc/5.4.0

source activate /bgfs/jkitzes/let110/envs/aldi

python -i tools/train_net.py --config configs/ALDI-XC-Song9.yaml