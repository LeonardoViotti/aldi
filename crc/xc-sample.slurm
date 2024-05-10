#!/bin/bash
#SBATCH --job-name=aldi-test
#SBATCH --output=out/aldi-test.out
#SBATCH --time=1-00:00:00
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

python tools/train_net.py --config configs/Base-XC-FPN-sample.yaml
