#!/usr/local/bin/python

from multiprocessing import Pool
import os

max_depth = os.getenv('MYTH_MAX_DEPTH')
sol_files = []
for root, dirs, files in os.walk(r"contracts/Contracts/"):
    for file in files:
        if file.endswith(".sol"):
            sol_files.append(os.path.join(root, file))


def analyze_contracts(filename):
    myth_cmd = "myth -v4 a"+" " + filename + " " + \
        "--solc-json remappings.json --max-depth " + max_depth + " -o jsonv2 | jq -r >pipeline-scripts/$(echo " + \
        filename+" | awk -F \"/\" '{print $NF}').json"
    os.system(myth_cmd)


def pool_handler():
    p = Pool(16)
    p.map(analyze_contracts, sol_files)


if __name__ == '__main__':
    pool_handler()
