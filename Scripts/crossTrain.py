#!/usr/bin/python

#Model params so far{
# Arg1: Model_name          = Any bert model with "ForSequenceClassificaiton task" from huggingface
# Arg2: Batch Size          = int
# Arg3: Warmup Steps        = int
# Arg4: Learning_Rate       = float
# Arg5: Weight_Decay        = float
# Arg6: Context Config        = List of different Context Config [1,2,3,4,5]
#                                   {
#                                       1: no context included

#                                       2: only context label pre original text
#                                       3: only context sender pre original text
#                                       4: only context text pre original text

#                                       5: only context label post original text
#                                       6: only context sender post original text
#                                       7: only context text post original text

#                                       8: context label + sender pre original text
#                                       9: context label + text pre original text
#                                       10: context label + sender + text pre original text
#                                       11: context label + text + sender pre original text
#                                       12: context sender + label pre original text
#                                       13: context sender + Text pre original text
#                                       14: context sender  + Label + Text pre original text
#                                       15: context sender + Text + Label pre original text
#                                       16: context text + sender pre original text
#                                       17: context text + label pre original text
#                                       18: context text + sender + label pre original text
#                                       19: context text + label + sender pre original text

#                                       20: context label + sender post original text
#                                       21: context label + text post original text
#                                       22: context label + sender + text post original text
#                                       23: context label + text + sender post original text
#                                       24: context sender + label post original text
#                                       25: context sender + Text post original text
#                                       26: context sender  + Label + Text post original text
#                                       27: context sender + Text + Label post original text
#                                       28: context text + sender post original text
#                                       29: context text + label post original text
#                                       30: context text + sender + label post original text
#                                       31: context text + label + sender post original text
#                                   }
# Arg7: Normalize Dataset   = Whether or not you want to use normalized Dataset created with MoNoice. Values are= <"normalized","regular">
# Arg8: Resampling Size     = float
# Arg9: Random_seed         = int
# Arg10: target Label       = <"Predicted","Gold">

import csv
import sys, os
import math
import random
import numpy as np
from pathlib import Path

from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

import torch

from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

from ContextConfig import ContextConfigCrossDomain

os.environ["TOKENIZERS_PARALLELISM"] = "false"
max_length = 512
sampling_seed = 1

model_name = sys.argv[1]
convert_batch_size = int(sys.argv[2])
convert_warmup_steps = int(sys.argv[3])
convert_learning_rate = float(sys.argv[4])
convert_weight_decay  = float(sys.argv[5])
convert_context_Config = int(sys.argv[6])
dataset_state = sys.argv[7]
resampling_size = float(sys.argv[8])
random_seed = int(sys.argv[9])
target_Label = sys.argv[10]


labelMappings = {
    "choiceQuestion":0,
    "inform":1,
    "misc":2,
    "greeting":3,
    "continuer":4,
    "agreement":5,
    "instruct":6,
    "negativeExpression":7,
    "setQuestion":8,
    "offer":9,
    "propositionalQuestion":10,
    "positiveExpression":11,
    "goodbye":12,
    "correction":13,
    "suggestion":14,
    "declineAction":15,
    "disagreement":16,
    "acceptAction":17,
    "elaborate":18
    }

def read_sourcefile(split_dir):
    split_dir = Path(split_dir)
    meta = []
    labels = []
    with open(split_dir, "r", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter = ";")
        header = next(reader)
        labelColumn = header.index("Label")
        for row in reader:
            if row[labelColumn] in labelMappings:
                meta.append(row[:labelColumn])
                label_name = labelMappings.get(row[labelColumn])
                labels.append(label_name)
            # else:
            #     print(row[labelColumn])
    file.close()
    return meta, labels

# Rob van der Goot, Ahmet ̈Ust ̈un, Alan Ramponi, andBarbara Plank. 2020a. MaChAmp proportional sam-pling. https://github.com/machamp-nlp/machamp/blob/master/machamp/modules/bucket_batch_sampler.py

def sample_smoothing(meta, labels, sampling_smoothing):
    
    uniqueLabels, distribution = np.unique(labels, return_counts=True)
    
    # sampling_smoothing: float = 1.0

    if sampling_smoothing != 1.0:   
        all_batches = []
        NPS_sorted = [list(x) for x in sorted(zip(NPS_Labels, NPS_Meta))]
        startCount = 0

        for labelCount in distribution:
            batch = []
            stopCount = startCount + labelCount
            for i in range(startCount, stopCount):
                batch.append(NPS_sorted[i])
            all_batches.append(batch)
            startCount = stopCount

        sizes = distribution
        total_size = sum(sizes)

        # calculate new size based on smoothing
        new_sizes = []
        total_new_prob = 0.0
        for size in sizes:
            pi = size/total_size
            total_new_prob += math.pow(pi, sampling_smoothing)

        for size in sizes:
            pi = size/total_size
            prob = (1/pi) * (math.pow(pi, sampling_smoothing)/total_new_prob)
            new_sizes.append(int(size * prob))
        # print(new_sizes)

        # collect all batches
        resampled_batches = []
        for dataset_idx in range(len(sizes)):
            new_size = new_sizes[dataset_idx]
            #random.shuffle(all_batches[dataset_idx])
            while new_size > len(all_batches[dataset_idx]):
                all_batches[dataset_idx] += all_batches[dataset_idx]
            resampled_batches += all_batches[dataset_idx][:new_size]

        # shuffle all batches
        random.seed(sampling_seed)
        random.shuffle(resampled_batches)
        # meta and label lists
        labels, meta = zip(*resampled_batches)
        return meta, labels

    else: 
        return meta, labels

def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    f1 = f1_score(labels, preds, average="weighted")
    return {'F1_Score': f1,}

class Dataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)    


device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=19)
model = model.to(device)

#Read data files for the models
if dataset_state == "normalized":
    NPS_Meta, NPS_Labels = read_sourcefile("../DataSets/MoNoice/NPS/NPS_MoNoice.csv")
    Reddit_Meta, Reddit_Labels = read_sourcefile("../DataSets/MoNoice/Reddit/Reddit_MoNoice.csv")
elif dataset_state =="regular":
    NPS_Meta, NPS_Labels = read_sourcefile("../DataSets/Training/npsChat/NPSChatTokenizedWithContext.csv")
    Reddit_Meta, Reddit_Labels = read_sourcefile("../DataSets/Target1/RedditConvoKit/RedditCorpusContext.csv")

NPS_Meta, NPS_Labels = sample_smoothing(NPS_Meta, NPS_Labels, resampling_size)

#NPS dataset splits
train_NPS_Meta, val_NPS_Meta, train_NPS_labels, val_NPS_labels = train_test_split(NPS_Meta, NPS_Labels, test_size=0.2, random_state=random_seed)
dev_NPS_Meta, test_NPS_Meta, dev_NPS_labels, test_NPS_labels = train_test_split(val_NPS_Meta, val_NPS_labels, test_size=0.5, random_state=random_seed)

# train_NPS_Meta, train_NPS_labels = sample_smoothing(train_NPS_Meta, train_NPS_labels, resampling_size)

#Reddit dataset splits
tune_Reddit_Meta, test_Reddit_Meta, tune_Reddit_labels, test_Reddit_labels = train_test_split(Reddit_Meta, Reddit_Labels, test_size=0.5, random_state=random_seed)


NPS_train_encodings = ""
NPS_dev_encodings = ""
Reddit_tune_encodings = ""
Reddit_test_encodings = ""



if convert_context_Config == 1:
    configger = ContextConfigCrossDomain(convert_context_Config,target_Label,train_NPS_Meta,dev_NPS_Meta,tune_Reddit_Meta,test_Reddit_Meta)
    NPS_train_text,NPS_dev_text,Reddit_tune_text,Reddit_test_text = configger.generateConfig()
    NPS_train_encodings = tokenizer(
        NPS_train_text,
        add_special_tokens=True,
        max_length=512,
        truncation=True, 
        padding=True, 
        return_tensors='pt'
        )

    NPS_dev_encodings = tokenizer(
        NPS_dev_text,
        add_special_tokens=True,
        max_length=512,
        truncation=True, 
        padding=True, 
        return_tensors='pt'
        )

    Reddit_tune_encodings = tokenizer(
        Reddit_tune_text, 
        add_special_tokens=True,
        max_length=512,
        truncation=True, 
        padding=True, 
        return_tensors='pt'
        )

    Reddit_test_encodings = tokenizer(
        Reddit_test_text, 
        add_special_tokens=True,
        max_length=512,
        truncation=True, 
        padding=True, 
        return_tensors='pt'
        )

else:
    configger = ContextConfigCrossDomain(convert_context_Config,target_Label,train_NPS_Meta,dev_NPS_Meta,tune_Reddit_Meta,test_Reddit_Meta)
    NPS_train_context_Pre, NPS_train_context_Post, NPS_dev_context_Pre, NPS_dev_context_Post, Reddit_tune_context_Pre, Reddit_tune_context_Post, Reddit_test_context_Pre, Reddit_test_context_Post = configger.generateConfig()
    
    NPS_train_encodings = tokenizer(
        NPS_train_context_Pre,
        NPS_train_context_Post,
        add_special_tokens=True,
        max_length=512,
        truncation=True, 
        padding=True, 
        return_tensors='pt'
        )

    NPS_dev_encodings = tokenizer(
        NPS_dev_context_Pre,
        NPS_dev_context_Post,
        add_special_tokens=True,
        max_length= 512,
        truncation=True, 
        padding=True, 
        return_tensors='pt'
        )

    Reddit_tune_encodings = tokenizer(
        Reddit_tune_context_Pre, 
        Reddit_tune_context_Post, 
        add_special_tokens=True,
        max_length=512,
        truncation=True, 
        padding=True, 
        return_tensors='pt'
        )

    Reddit_test_encodings = tokenizer(
        Reddit_test_context_Pre, 
        Reddit_test_context_Post, 
        add_special_tokens=True,
        max_length=512,
        truncation=True, 
        padding=True, 
        return_tensors='pt'
        )

NPS_train_dataset = Dataset(NPS_train_encodings, train_NPS_labels)
NPS_dev_dataset = Dataset(NPS_dev_encodings, dev_NPS_labels)
Reddit_tune_dataset = Dataset(Reddit_tune_encodings, tune_Reddit_labels)
Reddit_test_dataset = Dataset(Reddit_test_encodings, test_Reddit_labels)

model_params =  "-".join(str(input) for input in sys.argv[2:])
model_location_output = 'results/{model_name_for_output} - {model_params_name}'.format(model_name_for_output = model_name, model_params_name = model_params)



#Optimizer setup
training_args = TrainingArguments(
    output_dir = model_location_output,                 # output directory
    num_train_epochs = 5,                               # total number of training epochs
    per_device_train_batch_size = convert_batch_size,   # batch size per device during training
    per_device_eval_batch_size = 64,                    # batch size for evaluation
    warmup_steps = convert_warmup_steps,                # number of warmup steps for learning rate scheduler
    learning_rate = convert_learning_rate,              # Specify the learning rate
    weight_decay = convert_weight_decay,                # strength of weight decay
    logging_dir = './logs',                             # directory for storing logs
    load_best_model_at_end = True,                      # load the best model when finished training (default metric is loss)
    logging_strategy = "epoch",                         # The logging strategy to adopt during training
    evaluation_strategy = "epoch",                      # evaluate each `epoch`
    save_strategy = "epoch",                            # The checkpoint save strategy to adopt during training
    save_total_limit = 1,                               # Only retaining our best model
    metric_for_best_model ="F1_Score",                  # chocen evaluation metric
)

trainer = Trainer(
    model = model,                         # the instantiated Transformers model to be trained
    args = training_args,                  # training arguments, defined above
    train_dataset = NPS_train_dataset,     # training dataset
    eval_dataset = NPS_dev_dataset,        # evaluation dataset
    compute_metrics = compute_metrics      # Setting our compute metrics function as our desired function
)

trainer.train()

eval = trainer.evaluate(Reddit_tune_dataset)
# eval = trainer.evaluate(Reddit_test_dataset)


if convert_context_Config < 2:
    def get_prediction(text, model):
        inputs = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt").to(device)     # prepare our text into tokenized sequence
        outputs = model(**inputs)                                                                                   # perform inference to our model
        probs = outputs[0].softmax(1)                                                                               # get output probabilities by doing softmax
        return list(range(19))[probs.argmax()]                                                                      # executing argmax function to get the candidate label

    # model_predictions = []
    # for i in Reddit_test_text:
    #     model_predictions.append(get_prediction(i, model))

    model_predictions = []
    for i in Reddit_tune_text:
        model_predictions.append(get_prediction(i, model))
    
else:
    def get_prediction(pre,post, model):
        inputs = tokenizer(pre,post, padding=True, truncation=True, max_length=512, return_tensors="pt").to(device)  # Add .toDevice for later use on Cuda
        outputs = model(**inputs)
        probs = outputs[0].softmax(1)
        return list(range(19))[probs.argmax()]
    
    # model_predictions = []
    # for i in range(len(Reddit_tune_context_Pre)):
    #     model_predictions.append(get_prediction(Reddit_test_context_Pre[i],Reddit_test_context_Post[i], model))
    
    model_predictions = []
    for i in range(len(Reddit_tune_context_Pre)):
        model_predictions.append(get_prediction(Reddit_tune_context_Pre[i],Reddit_tune_context_Post[i], model))


# goldLabels = test_Reddit_labels
goldLabels = tune_Reddit_labels

# Directory
directory = model_name

if("/") in model_name:
    directory = (model_name.split("/")[-1]).replace("\\","")

# Parent Directory path
parent_dir = "../ModelEvaluations/" + directory + "-"+ model_params

print(parent_dir)
# Create Eval dir for model
path = os.path.join(parent_dir)
if(os.path.isdir(path)):
    if(os.path.isfile(path+"/eval")):
        file = open(path+"/eval", 'r')
        Lines = file.readlines()
        current_best_f1 = float(Lines[1].split("\t")[1])
        model_f1 = eval.get("eval_F1_Score")
        if(model_f1>current_best_f1):
            with open(path+"/eval", "w") as output:
                for key in eval.keys():
                    output.write(str(key)+"\t"+str(eval[key]))
                    output.write("\n")
                output.write("--------------------Model Information--------------------")
                output.write("\n")
                output.write("ModelName:\t" + model_name)
                output.write("\n")
                output.write("Parameters:\t" + model_params)
                output.write("\n")
                output.write("random seed:\t" + str(random_seed))
                output.write("\n")
                output.write("--------------------Training Arguments --------------------")
                output.write("\n")
                # print(training_args, file=open(path+"/eval", "a"))
            with open(path+"/cross_domain_predictions", "w") as output2:
                for pred in model_predictions:
                    output2.write(str(pred))
                    output2.write("\n")
            with open(path+"/goldLabels", "w") as output3:
                for gold in goldLabels:
                    output3.write(str(gold))
                    output3.write("\n")
        else:
            pass

    else:
        with open(path+"/eval", "w") as output:
            for key in eval.keys():
                output.write(str(key)+"\t"+str(eval[key]))
                output.write("\n")
                output.write("--------------------Model Information--------------------")
                output.write("\n")
                output.write("ModelName:\t" + model_name)
                output.write("\n")
                output.write("Parameters:\t" + model_params)
                output.write("\n")
                output.write("random seed:\t" + str(random_seed))
                output.write("\n")
                output.write("--------------------Training Arguments --------------------")
                output.write("\n")
                # print(training_args, file=open(path+"/eval", "a"))
            with open(path+"/cross_domain_predictions", "w") as output2:
                for pred in model_predictions:
                    output2.write(str(pred))
                    output2.write("\n")
            with open(path+"/goldLabels", "w") as output3:
                for gold in goldLabels:
                    output3.write(str(gold))
                    output3.write("\n")

else:
    os.mkdir(path)
    with open(path+"/eval", "w") as output:
        for key in eval.keys():
            output.write(str(key)+"\t"+str(eval[key]))
            output.write("\n")
        output.write("\n")
        output.write("--------------------Model Information--------------------")
        output.write("\n")
        output.write("ModelName:\t" + model_name)
        output.write("\n")
        output.write("Parameters:\t" + model_params)
        output.write("\n")
        output.write("random seed:\t" + str(random_seed))
        output.write("\n")
        output.write("--------------------Training Arguments --------------------")
        output.write("\n")
        # print(training_args, file=open(path+"/eval", "a"))
    with open(path+"/cross_domain_predictions", "w") as output2:
        for pred in model_predictions:
            output2.write(str(pred))
            output2.write("\n")
    with open(path+"/goldLabels", "w") as output3:
        for gold in goldLabels:
            output3.write(str(gold))
            output3.write("\n")  