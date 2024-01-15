# How to Become a Master of GreatLakes



## System structure
- Home directory: Only 80GB of storage, fills up quickly
- `/scratch/ahowens_root/ahowens1/`: 10TB shared across the lab. Data is automatically deleted if not accessed for 60 days
- `/nfs/turbo/coe-ahowens/`: Also 10TB, but no 60 day policy. Slower than scratch (still pretty fast though)
- `/tmpssd/`: 14TB of the fastest storage assigned by nodes, only accessible from a running job. Have to copy data in from scratch or turbo first

To preserve the file in scratch:
```bash
#/bin/bash
find ~/scratch/czyang -exec touch -ah {} \;
```

## Interactive section
Create a bash script with the template below

```bash
#/bin/bash

NUMGPU=$1
echo NUM_GPU=$NUMGPU

salloc \
--job-name=interactive_job \
--mail-user=czyang@umich.edu \
--mail-type=NONE \
--ntasks=1 \
--cpus-per-gpu=4 \
--mem-per-cpu=16GB \
--gres=gpu:$NUMGPU \
--time=01-00:00:00 \
--partition=spgpu \
--account=ahowens1
```

Remeber to quit it or cancel the job if you are not using.


## Lanuch jobs and monitor
- Create a bash script `myjob.sh` with the template below
```bash
#!/bin/bash

#SBATCH -p spgpu
#SBATCH --account=ahowens1
#SBATCH --job-name=FMA-StereoCRW-V2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --open-mode=append

#SBATCH --gres=gpu:1
#SBATCH --time=10-00:00:00
#SBATCH --mem-per-cpu=11G

# module load cuda/11.2.1  gcc/8.2.0
export LOGURU_LEVEL="INFO"

cd /home/czyang/Workspace/Learn-From-Stereo/StereoCRW

EXP='Final-GreatLake/PatchSpec-FreeMusic/EXP1.2-StereoCRW-V2-0.064S-ResNet9-4Stride-49num-0skipnode'
batch_size=48
num_workers=4

# running jobs
python main.py --exp=$EXP --epochs=80 --setting='aug_stereocrw_freemusic' --backbone='resnet9' --batch_size=$batch_size --num_workers=$num_workers --save_step=1 --valid_step=1 --lr=0.0001 --optim='AdamW' --repeat=1 --schedule='cos' --clip_length=0.064 --patch_stride=4 --patch_num=49 --wav2spec --aug_wave --regular_scaling --add_mixture --noiseSNR=40 --add_reverb --synthetic_rate=0.0 --crw_rate=1.0 --resume='PatchSpec-FreeMusic-New/EXP3.4-AugCRW-0.48S-ResNet9-4Stride-49num-0skipnode-RegularAugWave-AdamW-AddNoise-AddMixture/checkpoint_ep80.pth.tar'
```

- Lanuch job: `sbatch myjob.sh`
- Monitor the output: `tail -n 50 -f slurm-xxxx.out`





## Helpful commands
- Launch A Job: `sbatch job_file_name.sbat`
- View Lab GPU Usage: `my_account_resources ahowens1 -v`
- View Your Jobs: `sq`
- Cancel A Job: `scancel [JOBID]`
- View Job Output: `vim slurm-[JOBID].out`
- View V100 Availability:	`sstate -p gpu`
- View A40 Availability: `sstate -p spgpu`
- View /scratch Use: `scratch-quota ahowens_root`


## Install code-server for Greatlakes
- download code-server from [github](https://github.com/coder/code-server) and extract to home path or others. Here, we use v4.19.0 as an example, please use the latest version in the github:
```bash
wget https://github.com/coder/code-server/releases/download/v4.19.0/code-server-4.19.0-linux-amd64.tar.gz
tar -zxvf code-server-4.19.0-linux-amd64.tar.gz
```

- Lanuch code-server using tmux so that session won't be closed. 
```bash
cd code-server-4.19.0-linux-amd64/bin
./code-server --port 8082
```

- Open config.yaml for password:
```bash
cat /home/czyang/.config/code-server/config.yaml
```

- In the local machine, ssh with the specifc portal, and make sure you are ssh into the same login node. Then open the `http://localhost:8082/` in the Browse.
```
ssh -L 8082:localhost:8082 greatlake1  
```

- For easy use in the future, add the line below in the `~/.zshrc`, then you can launch code-server anywhere by `code-server --port 8082`:
```bash
alias code-server='sh ~/code-server-4.19.0-linux-amd64/bin/code-server'
```


## Guidance from others
- [Introduction to GreatLakes](https://docs.google.com/presentation/d/1ZnHSLA6WCXz-Ybdvz0OtFMok6IrSAzXS4nP6oQrfAOY/edit#slide=id.p)