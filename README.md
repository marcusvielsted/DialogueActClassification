## DialougeActClassificationThesis
Thesis project for "Increasing Robustness for Cross-domain Dialogue Act Classification on Social Media Data"
By Marcus Vielsted (Marcus.vielsted@gmail.com) & Nikolaj Wallenius (Nikolaj@wallenius.dk)

## Table of contents
* [DataSets](#Data-Sets)
* [Model Evaluation](#Model-Evaluation)
* [Scripts](#Scripts)
* [Setup](#Setup)
* [Usage](#Usage)

## DataSets
The dataset used for this project, are located in the rootfolder "DataSets". 

### Source Domain
* The Original NPS dataset used as our source domain for this project, can be found under "DataSets/Training/npsChat/NPSChatTokenizedWithContext.csv". As this dataset is publically available prior to this project, this additional folder within "DataSets/Training/npsChat/" originate from its creation by [EricForsyth et al., 2008](http://faculty.nps.edu/cmartell/NPSChat.htm)
* The lexical normalized version of our NPS dataset is located at "DataSets/MoNoice/NPS\NPS_MoNoice.csv"

### Target Domain
* Our original target dataset from reddit can be found in "DataSets/Target1/RedditConvoKit/RedditCorpusContext.csv"
* The script we used to create this dataset can be found in the same folder 
* The lexical normalized version of our Reddit dataset is located at "DataSets/MoNoice/NPS\Reddit_MoNoice.csv"

### Predicted Label Folds
* in the folder "DataSets/Folds/", we have the 5 folds for each of our previously mentioned dataset used for generation "Predicted Label". Each fold generates three different files;
* * One containing the ID's of the utterences used for training
* * one containing the ID's used to predict on
* * one containing the predicted labels for each of the ID's used within a given fold
* * each row of the predicted labels consistes of the following syntax \[UtterenceID, Utterence Text, GoldLabel, PredictedLabel\] The three additional information is used to accurately merge the predicted label back into our datasets


## Model Evaluation
This folder contains all the test from various fine-tuned models created throughout our experiments. Within our different overall test suites described below, each finetuned model have its own folder with 3 files - one with the gold label for a given setup, one with the predicted labels for said setup and one with evaluation information with regards to the performance of the model. Within this eval file various information can be found, most importante the eval_F1_Score.

The following subfolders account for our different overall test suits and consists of:
* __"Baselin"__: Our baseline model for both in-domain and cross-domain finetuned with 5 different seeds
* __"BestModels"__: Our best model for both in-domain and cross-domain finetuned with 5 different seeds
* __"deepsig"__: All of our significance testing. Each folder consists of two subfolder; "A" and "B", where A is the subject of the null-hyphothesis of which, we want to disprove
* __"FeatureCombinationTest"__: Our test suites for the best performing feature combinations for both in-domain and cross-domain
* __"GoldTesting"__: Feature isolation testing using the Gold context label
* __"PredTesting"__: Feature isolation testing using the Preddicted context label
* __"TestSetConfirmation"__: Final validatios test using the test-set  


## Scripts
Witin this folder, we have our main code implementations for the project. While most python files are utilities used by the authers of this report and will thus not be elaborated, the following are important to know, when running our code.

* "ContextConfig.py": This is our custom python classes responsible for generating context based on a configuration input. We have two classes, one for in-domain(class "ContextConfigInDomain") and one for cross-domain(class "ContextConfigCrossDomain"). __important note to know if implemented in your own code. When more than one context element is used, they get concatenated with " \[SEP\] ", since this is the sep-token for our transformer. This should be change so its suits your transformer model's sep-token__
* "CrossTrain.py": Our sourcecode for fine-tuning and evaluation a cross-domain setup. Usage will be explained further down in section [Usage](#Usage)
* "deepsig.py": The sourcecode for running a significance test. The prerequisite is to have created a folder within the "ModelEvaluations/deepsig" folder, with setup "A" and setup "B". Within these two subfolder, you must have an equal amount of models, but there is no limits as to how many
* "generateCrossParams.py": Utility. Used to generate the commandline input for runnig various model for our cross-domain setup. Creates a new folder names "ModelSetup" with a file names "modelList.txt" where each row corresponds to a commandline for running a given model with specific parameters and features. Calls the sourcecode of "crossTrain.py"
* "generateKFoldParams.py": Utility. Used to generate the commandline input for runnig various model for our KFold for generating predicted labels for our datasets. Creates a new folder names "ModelSetup" with a file names "modelList.txt" where each row corresponds to a commandline for running a given model with specific parameters and features. Calls the sourcecode of "KFoldPredictedTrainingLabels.py"
* "generateModelParams.py": Utility. Used to generate the commandline input for runnig various model for our in-domain setup. Creates a new folder names "ModelSetup" with a file names "modelList.txt" where each row corresponds to a commandline for running a given model with specific parameters and features. Calls the sourcecode of "train.py"
* "getBestModel.py": Utility. Iterates through all the eval.txt files within a subfolder of "ModelEvaluations" and prints all  the scores + the finds the best model
* "KFoldPredictedTrainingLabels.py": The sourcecode for running the 5 folds for generating our predicted labels. If you wanted more folds than five, this can be changed in line 139;
* *  skf = StratifiedKFold(n_splits=5, random_state=None, shuffle=False) // where n_splits can be changed
* "Setup.sh" : all our our dependencies for being able to run this project
* "slurmModelSetup.py": Utility. Helpful for batching and running all our the models within the "modelList.txt" file generated above on a linux server.
* "train.py" :  Our sourcecode for fine-tuning and evaluation a in-domain setup. Usage will be explained further down in section [Usage](#Usage)


## Setup
To run this project, install the following dependencies:
```
$ pip3 install -U scikit-learn
 
$ pip3 install transformers
 
$ pip3 install huggingface_hub
 
$ pip3 install torch torchvision torchaudio
 
$ pip3 install sentencepiece

$ pip3 install deepsig
```

## Usage
Running our in-domain("train.py") and our cross-domain("crossTrain.py") and be done in almost the same way. The only change i wheter you call `python train.py ...` or `python crossTrain.py ...`. Both scripts takes the same parameter which will be explained here
* Arg1: Model_name          -           Any bert model with "ForSequenceClassificaiton task" from huggingface
* Arg2: Batch Size          -           int
* Arg3: Warmup Steps        -           int
* Arg4: Learning_Rate       -           float
* Arg5: Weight_Decay        -           float
* Arg6: Context Config      -           the desired context configurations. range for 1-31
* * 1: no context included
* * 2: only context label pre original text
* * 3: only context sender pre original text
* * 4: only context text pre original text
* * 5: only context label post original text
* * 6: only context sender post original text
* * 7: only context text post original text
* * 8: context label + sender pre original text
* * 9: context label + text pre original text
* * 10: context label + sender + text pre original text
* * 11: context label + text + sender pre original text
* * 12: context sender + label pre original text
* * 13: context sender + Text pre original text
* * 14: context sender  + Label + Text pre original text
* * 15: context sender + Text + Label pre original text
* * 16: context text + sender pre original text
* * 17: context text + label pre original text
* * 18: context text + sender + label pre original text
* * 19: context text + label + sender pre original text
* * 20: context label + sender post original text
* * 21: context label + text post original text
* * 22: context label + sender + text post original text
* * 23: context label + text + sender post original text
* * 24: context sender + label post original text
* * 25: context sender + Text post original text
* * 26: context sender  + Label + Text post original text
* * 27: context sender + Text + Label post original text
* * 28: context text + sender post original text
* * 29: context text + label post original text
* * 30: context text + sender + label post original text
* * 31: context text + label + sender post original text
* Arg7: Normalize Dataset   -           Whether or not you want to use normalized Dataset created with MoNoice. Values are= <"normalized","regular">
* Arg8: Resampling Size     -           float
* Arg9: Random seeds        -           int
* Arg10: target Label       -           Whether Gold or Predicted context labels should be used. Values are= <"Predicted","Gold">



Having established a value for the parameters above, an example of how to run our cross-domain training could be the following command line
```
python3 train.py microsoft/deberta-v3-base 16 125 7e-05 0.5 28 regular 0.05 1 Gold
```

