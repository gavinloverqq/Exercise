# config.py 
import os
current_directory = os.path.dirname(os.path.abspath(__file__)) # 获取的是当前文件路径

# Join the relative path with the current directory path
read_relative_path =  "../input/mnist_train_folds.csv" 
TRAINING_FILE = os.path.join(current_directory, read_relative_path) 
 
model_relative_path = "../models/" 
MODEL_OUTPUT = os.path.join(current_directory, model_relative_path) 

MODEL = "decision_tree_entropy"