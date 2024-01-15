#!/usr/bin/env python
import os, sys
import numpy as np

print_offenders = False
print_users = False
print_accounts = False

if True:
    partition = "spgpu"
    mem_to_gpu = 48
    cpu_to_gpu = 4
else:
    partition = "gpu"
    mem_to_gpu = 90
    cpu_to_gpu = 20


if len(sys.argv) > 1:
    if sys.argv[1] == "offenders":
        print_offenders = True
    elif sys.argv[1] == "users":
        print_users = True
    elif sys.argv[1] == "accounts":
        print_accounts = True
    else:
        print("Unknown option: ", sys.argv[1])
else:
    print_offenders = True
    print_users = True
    print_accounts = True


jobs = os.popen(
    f"squeue -O 'JobArrayID:.14 ,UserName:.90 ,Account:.90 ,ReasonList:90 ,tres-alloc:90' -p {partition}"
).read()

# split by new line .. first and last are bad
jobs = jobs.split("\n")[1:-1]
jobs = [job.split() for job in jobs]

# remove non running jobs
jobs = [_j for _j in jobs if "gl" in _j[3]]

# parse them
for i in range(len(jobs)):
    res = jobs[i][4].split(",")
    res = [res[0], res[1], res[4]]
    cpu, mem, gpu = [_r.split("=")[1] for _r in res]
    cpu, gpu = int(cpu), int(gpu)

    # convert M
    if mem[-1] == "G":
        mem = float(mem[:-1])
    elif mem[-1] == "M":
        mem = float(mem[:-1]) / 1000
    else:
        raise ValueError("How to parse memory: ", mem)

    account = jobs[i][2]
    if account[-1] in [str(i) for i in range(9)]:
        account = account[:-1]
        jobs[i][2] = account

    jobs[i].append((cpu, mem, gpu))


# figure out which jobs do not conform to config and why
nonconf_memgpu, nonconf_cpugpu, nonconf_memcpu = [], [], []
nonconf_id, nonconf_user, nonconf_account = [], [], []

user_dict, account_dict = {}, {}

for job in jobs:
    job_id, user, account, reason, tres, res = job
    cpu, mem, gpu = res

    if user in user_dict:
        user_dict[user][0] += cpu
        user_dict[user][1] += mem
        user_dict[user][2] += gpu
    else:
        user_dict[user] = [cpu, mem, gpu]

    if account in account_dict:
        account_dict[account][0] += cpu
        account_dict[account][1] += mem
        account_dict[account][2] += gpu
    else:
        account_dict[account] = [cpu, mem, gpu]

    if cpu / gpu > cpu_to_gpu:
        ratio = cpu / gpu / cpu_to_gpu
        nonconf_cpugpu.append(f"- {ratio:7.2f}x    {user:20}  {account:20}  {tres}")
        nonconf_id.append(job_id)
        nonconf_user.append(user)
        nonconf_account.append(account)

    # if mem / cpu > 12:
    #     ratio = mem / cpu / 12.
    #     nonconf_memcpu.append(f"- {ratio:7.2f}x    {user:20}  {account:20}  {tres}")
    #     nonconf_id.append(job_id)
    #     nonconf_user.append(user)
    #     nonconf_account.append(account)

    if mem / gpu > mem_to_gpu:
        ratio = mem / gpu / mem_to_gpu
        nonconf_memgpu.append(f"- {ratio:7.2f}x    {user:20}  {account:20}  {tres}")
        nonconf_id.append(job_id)
        nonconf_user.append(user)
        nonconf_account.append(account)

nonconf_user = set(nonconf_user)
nonconf_account = set(nonconf_account)
nonconf_id = set(nonconf_id)


if print_offenders:
    print(f"Number of non-conforming jobs: {len(nonconf_id)}/{len(jobs)} \n")

    print(f"Jobs came from {len(nonconf_user)} users:")
    [print(user) for user in nonconf_user]

    print()
    print(f"Jobs came from {len(nonconf_account)} accounts:")
    [print(acc) for acc in nonconf_account]
    print()

    print("Details:")
    print(f"Non-conforming CPU/GPU ratio ({len(nonconf_cpugpu)}):")
    [print(_j) for _j in nonconf_cpugpu]
    print()

    # print(f"Non-conforming MEM/CPU ratio ({len(nonconf_memcpu)}):")
    # [print(_j) for _j in nonconf_memcpu]
    # print()

    print(f"Non-conforming MEM/GPU ratio ({len(nonconf_memgpu)}):")
    [print(_j) for _j in nonconf_memgpu]
    print()

if print_users:
    print("=" * 57)
    print(f"{'User':20} |  {'Memory (in GB)':^8}     {'CPU':^4}     {'GPU':^4}")
    print("=" * 57)
    printout = []
    gpus = []
    for user in user_dict:
        cpu, mem, gpu = user_dict[user]
        printout.append(f"{user:20} |  {mem:8.0f}     {cpu:4d}     {gpu:4d}")
        gpus.append(gpu)

    gpus = np.array(gpus)
    [print(printout[i]) for i in np.argsort(-1 * np.array(gpus))]
    print("=" * 57)

if print_accounts:
    print("=" * 57)
    print(f"{'Account':20} |  {'Memory (in GB)':^8}     {'CPU':^4}     {'GPU':^4}")
    print("-" * 57)
    printout = []
    gpus = []
    for account in account_dict:
        cpu, mem, gpu = account_dict[account]
        printout.append(f"{account:20} |  {mem:8.0f}     {cpu:4d}     {gpu:4d}")
        gpus.append(gpu)

    gpus = np.array(gpus)
    [print(printout[i]) for i in np.argsort(-1 * np.array(gpus))]
    print("=" * 57)