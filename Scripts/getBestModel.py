import os
import sys

rootdir = '../ModelEvaluations'

if len(sys.argv) < 2:
    print('please provide folder path in: ' + rootdir)
    exit(1)

folder = sys.argv[1]
folderPath = '/'.join([rootdir, folder])

bestModel = ""
bestEval = 0.0
evalLine = 1

for dirs in os.listdir(folderPath):
    evalFile = '/'.join([folderPath, dirs, 'eval'])
    # print(evalFile)
    try:
        with open(evalFile) as file:
            # print("opened")
            for position, line in enumerate(file):
                if position == evalLine:
                    print("Model: " + dirs)
                    print(line)
                    print("____________________________________________________\n")
                    evalScore = line.split("\t")[1]
                    evalScore = float(evalScore.strip())
                    if evalScore > bestEval:
                        bestEval = evalScore
                        bestModel = dirs
    except:
        pass
    
print("Best model = " + bestModel + " with an F1 score of: " + str(bestEval))
