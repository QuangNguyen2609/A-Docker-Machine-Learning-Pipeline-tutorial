# Versioning data.
import os
from dotenv import dotenv_values
config = dotenv_values(".env")
from pymongo import MongoClient
import glob


print('------Versioning data--------')

train_folder = glob.glob("./train/*")
validation_foler = glob.glob("./validation/*")

# Update training.

# {
# train: {
#   dogs: [],
#   cats: []
# }
# 
# []
# validation: []
# }

train = {}
for label_folder in train_folder:
    # print(label_folder)
    label_name = os.path.basename(label_folder)
    files = glob.glob('{}/*'.format(label_folder))
    train[label_name] = []
    for file in files:
        file_name = os.path.basename(file)
        # train[]
        train[label_name].append(file_name)

# print(train)

valid = {}
for label_folder in validation_foler:
    # print(label_folder)
    label_name = os.path.basename(label_folder)
    files = glob.glob('{}/*'.format(label_folder))
    valid[label_name] = []
    for file in files:
        file_name = os.path.basename(file)
        # valid[]
        valid[label_name].append(file_name)

# print(valid)

object_to_upload = {
    "train": train,
    "validation": valid,
}

print(train, valid)
mongodb_client = MongoClient(config['ATLAS_URI'])

# Raw data
database = mongodb_client['training']

database['dog-cats-training'].insert_one(object_to_upload)

print('------End Versioning--------')










