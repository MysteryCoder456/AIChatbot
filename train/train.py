#  Standard imports
import json

# import tensorflow as tf
# from tensorflow import keras
import numpy as np
import english_words

with open("classes.txt", "r") as classes_file:
    class_names = [class_name.replace("\n", "").strip() for class_name in classes_file.readlines()]

print(class_names)

words_list = list(english_words.english_words_lower_alpha_set)

sentence_limit = 10
training_data = []
training_labels = []

with open("train/training_data.json", "r") as data:
    raw_training_data = json.load(data)

# Convert strings to integers
for class_name in raw_training_data:
    for text in raw_training_data[class_name]:
        encoded_text = []

        for word in text.split():
            encoded_text.append(words_list.index(word))

        while len(encoded_text) < sentence_limit:
            encoded_text.append(0)

        while len(encoded_text) > sentence_limit:
            encoded_text.pop(-1)

        training_data.append(encoded_text)
        training_labels.append(class_names.index(class_name))
        print(encoded_text, class_name)

# print(training_data)
