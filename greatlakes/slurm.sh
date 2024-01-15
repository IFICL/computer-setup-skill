#!/bin/bash

#SBATCH -p spgpu              # Specifies the partition (queue) to submit the job to (spgpu in this case)
#SBATCH --account=ahowens1    # Specifies the account to which the job's resource usage will be charged
#SBATCH --job-name=PDM        # Specifies a name for the job
#SBATCH --ntasks-per-node=1   # Specifies the number of tasks (processes) to run on each node
#SBATCH --cpus-per-gpu=4      # Specifies the number of CPU cores to allocate per GPU
#SBATCH --open-mode=append    # Specifies the mode for opening files (append in this case)

#SBATCH --gres=gpu:1          # Specifies the number of GPUs to allocate (1 GPU in this case)
#SBATCH --time=6-00:00:00     # Specifies the maximum time the job will run (6 days in this case)
#SBATCH --mem-per-cpu=11G     # Specifies the amount of memory to allocate per CPU core

#SBATCH --output=slurm-logs/%j_out.log   # Specifies the output log file
#SBATCH --error=slurm-logs/%j_err.log    # Specifies the error log file

# module load cuda/11.2.1  gcc/8.2.0
{
export LOGURU_LEVEL="INFO"


source ~/.bashrc
zsh
conda activate pdm
cd /home/czyang/Workspace/perspective-diffusion/perspective-guided-diffusion


gpustat

# python main.py experiment=perspective_field task_name="perspective_field/exp_1" operator.forward_guidance_weight=10000.0
# python main.py experiment=perspective_field task_name="perspective_field/exp_2" operator.forward_guidance_weight=5000.0
# python main.py experiment=perspective_field task_name="perspective_field/exp_3" operator.forward_guidance_weight=2000.0
# python main.py experiment=perspective_field task_name="perspective_field/exp_4" operator.forward_guidance_weight=1000.0
# python main.py experiment=baselines/kitchen
# python main.py experiment=perspective_field/kitchen
python main.py experiment=perspective_field/kitchen_4





}