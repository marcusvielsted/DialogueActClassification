import sys
import os

run = True
path = "../ModelSetup/"

if not os.path.isdir('../ModelSetup'):
    os.mkdir('../ModelSetup')

if len(sys.argv) < 4:
    print('please provide: model list from path: ' + path + ', job name, and time (hours)')
    exit(1)

setupPath = path + sys.argv[1]


def makeFile(name, task, idx, time):
    name = name + '.' + str(idx)
    outFile = open(path + name + '.job', 'w')
    outFile.write('#!/bin/bash\n')
    outFile.write('\n')
    outFile.write('#SBATCH --job-name=' + name + '\n')
    outFile.write('#SBATCH --output=' + name + '.out\n')
    outFile.write('#SBATCH --cpus-per-task=2\n')
    outFile.write('#SBATCH --time=' + time + ':00:00\n')
    outFile.write('#SBATCH --gres=gpu\n')
    outFile.write('#SBATCH --mem=15G\n')
    outFile.write('#SBATCH --mail-type=BEGIN,END,FAIL\n')
    outFile.write('#SBATCH --partition=brown\n')
    # outFile.write('#SBATCH --nodelist=desktop17\n')
    # outFile.write('#SBATCH --partition=red\n')

    outFile.write('\n')
    outFile.write(task)
    if run:
        cmd = 'sbatch ' + name + '.job'
        # os.system(cmd)
        print(cmd)
    outFile.close()
    # cmd = 'sed -i "s;device [0-9];device \$CUDA_VISIBLE_DEVICES;g" ' + name + '.job'
    # os.system(cmd)

jobSize = 1
if len(sys.argv) > 4:
    jobSize = int(sys.argv[4])
concat = ''
counter = 0
for lineIdx, line in enumerate(open(setupPath)):
    if len(line) < 2:
        continue
    if lineIdx % jobSize == 0 and concat != '':
        makeFile(sys.argv[2], concat, counter, sys.argv[3])
        counter += 1
        concat = ''
    concat += line
if concat != '':
    makeFile(sys.argv[2], concat, counter, sys.argv[3])
