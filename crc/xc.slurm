#!/bin/bash
#SBATCH --job-name=dmixup-3000
#SBATCH --output=out/crc-7-dmixup-3000.out
#SBATCH --time=1-00:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=10
#SBATCH --cpus-per-task=1
#SBATCH --cluster=gpu
#SBATCH --partition=a100
#SBATCH --gres=gpu:1
#SBATCH --mem=100G

module purge
module load python/ondemand-jupyter-python3.9

source activate /bgfs/jkitzes/let110/envs/aldi

python -i tools/train_net.py --config configs/Base-XC-FPN.yaml