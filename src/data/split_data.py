import argparse
import pandas as pd
from load_data import read_params
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def split_data(df,train_data_path,test_data_path,split_ratio,random_state):
    df=df.dropna()
    train, test = train_test_split(df, test_size=split_ratio, random_state=random_state)
    train.to_csv(train_data_path, sep=",", index=False, encoding="utf-8")
    test.to_csv(test_data_path, sep=",", index=False, encoding="utf-8")    

def split_and_saved_data(config_path):
    config = read_params(config_path)
    raw_data_path = "data/raw/winequality.csv"
    test_data_path = "data/processed/winequality_test.csv" 
    train_data_path = "data/processed/winequality_test.csv"
    split_ratio = 0.2
    random_state = 42
    raw_df=pd.read_csv(raw_data_path)
    split_data(raw_df,train_data_path,test_data_path,split_ratio,random_state)
    
if __name__=="__main__":
    split_and_saved_data()