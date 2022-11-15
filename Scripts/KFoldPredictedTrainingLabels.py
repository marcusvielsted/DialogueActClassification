#!/usr/bin/python

#Model params so far{
# Arg1: Model_name          = Any bert model with "ForSequenceClassificaiton task" from huggingface
# Arg2: Batch Size          = int
# Arg3: Warmup Steps        = int
# Arg4: Learning_Rate       = float
# Arg5: Weight_Decay        = float
# Arg6: Context Config      = Run with no context. context = 1
# Arg7: Normalize Dataset   = Whether or not you want to use normalized Dataset created with MoNoice. Values are= <"normalized","regular">
# Arg8: Random seeds        = int
# Arg9: kfoldDataset       = <NPS,Reddit>

import re
import csv
import sys, os
from pathlib import Path
from sklearn.model_selection import StratifiedKFold

from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

import torch

from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

from ContextConfig import ContextConfigInDomain

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
random_seed = int(sys.argv[8])
DatasetSource = sys.argv[9]

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

 # __________________________________________________METHODS__________________________________________________

def get_key(val):
    for key, value in labelMappings.items():
         if val == value:
             return key
         
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

def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    # calculate accuracy using sklearn's function
    f1 = f1_score(labels, preds, average="weighted")
    return {'F1_Score': f1}

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


#Read data files for the models
if DatasetSource == "NPS":
    if dataset_state == "normalized":
        Meta, Labels = read_sourcefile("../DataSets/MoNoice/NPS/NPS_MoNoice.csv")
    elif dataset_state =="regular":
        Meta, Labels = read_sourcefile("../DataSets/Training/npsChat/NPSChatTokenizedWithContext.csv")
elif DatasetSource == "Reddit":
    if dataset_state == "normalized":
        Meta, Labels = read_sourcefile("../DataSets/MoNoice/Reddit/Reddit_MoNoice.csv")
    elif dataset_state =="regular":
        Meta, Labels = read_sourcefile("../DataSets/Target1/RedditConvoKit/RedditCorpusContext.csv")


train_Meta = Meta
train_Labels = Labels

# train_Meta, val_Meta, train_Labels, val_Labels = train_test_split(Meta, Labels, test_size=0.2, random_state=random_seed)
# dev_Meta, test_Meta, dev_Labels, test_Labels = train_test_split(val_Meta, val_Labels, test_size=0.5, random_state=random_seed)


# for i in dev_Meta:
#     train_Meta.append(i)
    
# for i in dev_Labels:
#     train_Labels.append(i)
    

skf = StratifiedKFold(n_splits=5, random_state=None, shuffle=False)
currentFold = 1
for train_index, dev_index in skf.split(train_Meta, train_Labels):
    # print("TRAIN:", train_index, "TEST:", dev_index)
    currentFoldTrainValues = []
    currentFoldTrainId = []
    currentFoldTrainLabels = []
    currentFoldDevValues = []
    currentFoldDevId = []
    currentFoldDevLabels = []
    
    for train_index_values in train_index:
        newLine = train_Meta[train_index_values]
        newLineID = train_Meta[train_index_values][0]
        newLineLabel = train_Labels[train_index_values]
        currentFoldTrainValues.append(newLine)
        currentFoldTrainId.append(newLineID)
        currentFoldTrainLabels.append(newLineLabel)
        
    for dev_index_values in dev_index:
        newLine = train_Meta[dev_index_values]
        newLineID = train_Meta[dev_index_values][0]
        newLinelabel = train_Labels[dev_index_values]
        currentFoldDevValues.append(newLine)
        currentFoldDevId.append(newLineID)
        currentFoldDevLabels.append(newLinelabel)
        
    
    with open("../DataSets/Folds/{Domain}_{DatasetState}/Trainfold{fold}".format(Domain=DatasetSource, DatasetState=dataset_state ,fold=currentFold),'w') as myfile:
        for Id in currentFoldTrainId:
            myfile.write(Id)
            myfile.write("\n")

     
    with open("../DataSets/Folds/{Domain}_{DatasetState}/Devfold{fold}".format(Domain=DatasetSource, DatasetState=dataset_state ,fold=currentFold),'w') as myfile:
        for Id in currentFoldDevId:
            myfile.write(Id)
            myfile.write("\n")
    
    train_Meta_post = currentFoldTrainValues
    train_Labels_post = currentFoldTrainLabels
    dev_Meta_post = currentFoldDevValues
    dev_Labels_post = currentFoldDevLabels
    
       
    train_encodings = ""
    dev_encodings = ""
    test_encodings = ""

    
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=19)
    model = model.to(device)
    
    train_text_only = []
    dev_text_only = []
    for text in train_Meta_post:
        train_text_only.append(text[3])
    for text in dev_Meta_post:
        dev_text_only.append(text[3])

    
    train_encodings = tokenizer(
        train_text_only,
        add_special_tokens=True,
        max_length=512,
        truncation=True, 
        padding=True, 
        return_tensors='pt'
        )

    dev_encodings = tokenizer(
        dev_text_only,
        add_special_tokens=True,
        max_length= 512,
        truncation=True, 
        padding=True, 
        return_tensors='pt'
        )

    # test_encodings = tokenizer(
    #     test_text_only, 
    #     add_special_tokens=True,
    #     max_length= 512,
    #     truncation=True, 
    #     padding=True, 
    #     return_tensors='pt'
    #     )
    # #____________________________________________________________________________________________________________________________

    train_dataset = Dataset(train_encodings, train_Labels_post)
    dev_dataset = Dataset(dev_encodings, dev_Labels_post)
    # test_dataset = Dataset(test_encodings, test_Labels)


    model_params =  "-".join(str(input) for input in sys.argv[2:])
    model_location_output = 'results/{model_name_for_output} - {model_params_name}'.format(model_name_for_output = model_name, model_params_name =model_params)


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
        metric_for_best_model="F1_Score",                   # chocen evaluation metric
    )

    trainer = Trainer(
        model=model,                         # the instantiated Transformers model to be trained
        args=training_args,                  # training arguments, defined above
        train_dataset=train_dataset,         # training dataset
        eval_dataset=dev_dataset,            # evaluation dataset
        compute_metrics=compute_metrics      # Setting our compute metrics function as our desired function
    )

    trainer.train()

    def get_prediction(text, model):
        # prepare our text into tokenized sequence
        inputs = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt").to(device)  # Add .toDevice for later use on Cuda
        # perform inference to our model
        outputs = model(**inputs)
        # get output probabilities by doing softmax
        probs = outputs[0].softmax(1)
        # executing argmax function to get the candidate label
        return list(range(19))[probs.argmax()]

    model_predictions =[]
    for i in dev_text_only:
        model_predictions.append(get_prediction(i, model))

    with open("../DataSets/Folds/{Domain}_{DatasetState}/Predictionsfold{fold}".format(Domain=DatasetSource, DatasetState=dataset_state, fold=currentFold),'w') as myfile:
        for idx, val in enumerate(model_predictions):
            myfile.write(dev_Meta_post[idx][0])
            myfile.write(";")
            myfile.write(dev_Meta_post[idx][3])
            myfile.write(";")
            myfile.write(get_key(dev_Labels_post[idx]))
            myfile.write(";")
            myfile.write(get_key(val))
            myfile.write("\n")
        
    currentFold = currentFold+1
    
    

   