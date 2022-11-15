import os
import sys
import numpy as np
from deepsig import aso

rootdir = '..\ModelEvaluations\Deepsig'

if len(sys.argv) < 2:
    print('Please provide folder name in path: ' + rootdir)
    exit(1)

evalLine = 1
testFolder = sys.argv[1]
confidence_level = 0.05

my_model_scores = []
my_model_name = ''
baseline_scores = []
baseline_name = ''


pathModelA = os.path.join(rootdir, testFolder, 'A')
pathModelB = os.path.join(rootdir, testFolder, 'B')

if(not os.path.isdir(pathModelA) or not os.path.isdir(pathModelB)):
    print('Proper file structure not in place for path:' + pathModelA + ' or ' + pathModelB)
    print('Please check that the correct folder name was used contrinaing the subfolders "A" and "B"')
    exit(1)

for dirs in os.listdir(pathModelA):
    evalFile = os.path.join(pathModelA, dirs, 'eval')
    if(not my_model_name):
        my_model_name = dirs
    try:
        with open(evalFile) as file:
            # print("opened")
            for position, line in enumerate(file):
                if position == evalLine:
                    evalScore = line.split("\t")[1]
                    evalScore = float(evalScore.strip())
                    my_model_scores.append(evalScore)
    except:
        print("No eval file found for: " + evalFile)
for dirs in os.listdir(pathModelB):
    evalFile = os.path.join(pathModelB, dirs, 'eval')
    if(not baseline_name):
        baseline_name = dirs
    try:
        with open(evalFile) as file:
            # print("opened")
            for position, line in enumerate(file):
                if position == evalLine:
                    evalScore = line.split("\t")[1]
                    evalScore = float(evalScore.strip())
                    baseline_scores.append(evalScore)
    except:
        print("No eval file found for: " + evalFile)

print("A scores: ", my_model_scores)
print("B scores: ", baseline_scores)

N = len(my_model_scores)  # Number of random seeds
min_eps = aso(my_model_scores, baseline_scores, confidence_level=confidence_level)
print("{:.5f}".format(min_eps))


sigPath = os.path.join(rootdir, testFolder, "significanceScore.txt")
with open(sigPath, "w") as output:
    output.write("_______________________________Deep Significance_______________________________")
    output.write("\n")
    output.write("Confidence level:\t" + str(confidence_level))
    output.write("\n")
    output.write("Minimum epsilon:\t" + "{:.5f}".format(min_eps))
    output.write("\n")
    output.write("Model A:\t" + my_model_name)
    output.write("\n")
    output.write("A scores:\t")
    output.writelines(", {:.5f}".format(score) for score in my_model_scores)
    output.write("\n")
    output.write("vs.")
    output.write("\n")
    output.write("Model B:\t" + baseline_name)
    output.write("\n")
    output.write("B scores:\t")
    output.writelines(", {:.5f}".format(score) for score in baseline_scores)
    output.write("\n")
