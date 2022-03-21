# How to Become a Master of GreatLakes



## System structure
- Home directory: Only 80GB of storage, fills up quickly
- `/scratch/ahowens_root/ahowens1/`: 10TB shared across the lab. Data is automatically deleted if not accessed for 60 days
- `/nfs/turbo/coe-ahowens/`: Also 10TB, but no 60 day policy. Slower than scratch (still pretty fast though)
- `/tmpssd/`: 14TB of the fastest storage assigned by nodes, only accessible from a running job. Have to copy data in from scratch or turbo first


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






## Helpful commands
- Launch A Job: `sbatch job_file_name.sbat`
- View Lab GPU Usage: `my_account_resources ahowens1 -v`
- View Your Jobs: `sq`
- Cancel A Job: `scancel [JOBID]`
- View Job Output: `vim slurm-[JOBID].out`
- View V100 Availability:	`sstate -p gpu`
- View A40 Availability: `sstate -p spgpu`
- View /scratch Use: `scratch-quota ahowens_root`


## Guidance from others
- [Introduction to GreatLakes](https://docs.google.com/presentation/d/1ZnHSLA6WCXz-Ybdvz0OtFMok6IrSAzXS4nP6oQrfAOY/edit#slide=id.p)
- 
