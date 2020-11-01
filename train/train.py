#  Standard imports
import json

# import tensorflow as tf
# from tensorflow import keras
import numpy as np

with open("classes.txt", "r") as classes_file:
    classes = [class_name.replace("\n", "").strip() for class_name in classes_file.readlines()]

print(classes)

training_data = []
testing_data = []

# preprocess data
