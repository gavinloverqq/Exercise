import pandas as pd 
from sklearn import model_selection 
import os
 
 
if __name__ == "__main__": 
    # Get the current directory path
    # current_directory = os.getcwd() # 获取的是执行路径
    current_directory = os.path.dirname(os.path.abspath(__file__)) # 获取的是当前文件路径

    # Join the relative path with the current directory path
    read_relative_path = "../input/train.csv"
    read_path = os.path.join(current_directory, read_relative_path)
    write_relative_path = "../input/train_folds.csv"
    write_path = os.path.join(current_directory, write_relative_path)
    
    df = pd.read_csv(read_path) 
     
    df["kfold"] = -1  # 创建一个名为 kfold 的新列，并用-1填充
    df = df.sample(frac=1).reset_index(drop=True) # 打乱数据 
    
    # fetch labels
    y = df.target.values
    # initiate the kfold class from model_selection module
    kf = model_selection.StratifiedKFold(n_splits=5)
    
    for fold, (trn_, val_) in enumerate(kf.split(X=df, y=y)): # 填充新的 kfold 列
        df.loc[val_, 'kfold'] = fold 
  
    df.to_csv(write_path, index=False) # 保存划分好的数据集