#!/bin/bash

read -p "Enter the partition [spgpu (A40) | gpu (V100) | standard (CPU)]: " partition

# Check the value of the partition and customize prompts accordingly
if [ "$partition" == "spgpu" ] || [ "$partition" == "gpu" ]; then
    read -p "Enter the number of GPUs: " numgpu
    if [ "$numgpu" -eq 0 ]; then
        echo "Error: Number of GPUs must be greater than 0 for the selected partition."
        exit 1
    fi
else
    numgpu=0
fi


# Check if the number of GPUs is 0
if [ "$numgpu" -eq 0 ]; then
    read -p "Enter the number of CPUs per task for CPU-only job: " numcpu
    cpu_config="--cpus-per-task=${numcpu}"
    account_config="--account=ahowens0"
else
    read -p "Enter the number of CPUs per GPU: " numcpu
    cpu_config="--cpus-per-gpu=${numcpu}"
    account_config="--account=ahowens1"
fi

read -p "Enter the number of memory per CPU: " nummem
read -p "Enter the time of request: " time

salloc \
--job-name=interactive_job \
--mail-user=czyang@umich.edu \
--mail-type=NONE \
--ntasks=1 \
--gres=gpu:${numgpu} \
${cpu_config} \
--mem-per-cpu=${nummem} \
--time=${time}-00:00:00 \
--partition=$partition \
${account_config}