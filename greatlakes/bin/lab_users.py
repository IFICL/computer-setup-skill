#!/usr/bin/env python
import sys
import os

if len(sys.argv) == 1:
    account_tar = "ahowens1"
else:
    account_tar = sys.argv[1]

jobs = os.popen(
    "squeue -O 'JobArrayID:.14 ,UserName:.90 ,Account:.90 ,ReasonList:90 ,tres-alloc:90'"
).read()

jobs = jobs.split("\n")[1:-1]
jobs = [job for job in jobs if account_tar in job]
jobs = [job.split() for job in jobs]

# remove non running jobs
jobs = [_j for _j in jobs if "gl" in _j[3]]

# parse them
for i in range(len(jobs)):
    res = jobs[i][4].split(",")

    if len(res) > 4:
        res = [res[0], res[1], res[4]]
        cpu, mem, gpu = [_r.split("=")[1] for _r in res]
        cpu, gpu = int(cpu), int(gpu)
    else:
        res = [res[0], res[1]]
        cpu, mem = [_r.split("=")[1] for _r in res]
        cpu, gpu = int(cpu), 0

    # convert M
    if mem[-1] == "G":
        mem = float(mem[:-1])
    elif mem[-1] == "M":
        mem = float(mem[:-1]) / 1000
    else:
        raise ValueError("How to parse memory: ", mem)

    jobs[i].append((cpu, mem, gpu))

total_mem = 0
total_cpu = 0
total_gpu = 0
user_usage = {}

for job in jobs:
    job_id, user, account, reason, tres, res = job
    cpu, mem, gpu = res
    if account_tar in account:
        total_mem += mem
        total_gpu += gpu
        total_cpu += cpu

        if user in user_usage:
            user_usage[user][0] += mem
            user_usage[user][1] += gpu
            user_usage[user][2] += cpu
        else:
            user_usage[user] = [mem, gpu, cpu]


print("=" * 57)
print(f"{'User':20} |  {'Memory (in GB)':^14}     {'CPU':^4}     {'GPU':^4}")
print("-" * 57)
for user in user_usage:
    mem, gpu, cpu = user_usage[user]
    print(f"{user:20} |  {mem:14.0f}     {cpu:4d}     {gpu:4d}")
print("-" * 57)
print(f"{'total':20} |  {total_mem:14.0f}     {total_cpu:4d}     {total_gpu:4d}")

if account_tar == "ahowens1":
    print(f"{'allocation':20} |  {'1920':>14}     {'160':>4}     {'40':>4}")
print("=" * 57)
