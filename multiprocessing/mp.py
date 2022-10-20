#!/usr/local/bin/python

import time
import multiprocessing
import os
import pdb

# list to store sol files
sol_files = []
for root, dirs, files in os.walk(r"contracts/Contracts/"):
    for file in files:
        if file.endswith(".sol"):
            sol_files.append(os.path.join(root, file))


def analyze_contracts(filename):
    myth_cmd = "myth -v5 a"+" " + filename + " " + \
        "--solc-json remappings.json --max-depth 15 -o jsonv2 | jq -r >pipeline-scripts/$(echo " + \
        filename+" | awk -F \"/\" '{print $NF}').json"
    os.system(myth_cmd)


if __name__ == '__main__':
    start = time.perf_counter()

    processes = [multiprocessing.Process(target=analyze_contracts, args=[filename])
                 for filename in sol_files]

    # start the processes
    for process in processes:
        process.start()

    # wait for completion
    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'It took {finish-start: .2f} second(s) to finish')
