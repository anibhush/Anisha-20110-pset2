import argparse
import pandas as pd 

def load_data(data_path,model_var):
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    df=df[model_var]
    return df

def load_raw_data():
    external_data_path="data/external/winequality.csv"
    raw_data_path="data/raw/winequality.csv"
    model_var=['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol','quality']

    
    df=load_data(external_data_path,model_var)
    df.to_csv(raw_data_path,index=False)
    
if __name__ == "__main__":
    args = argparse.ArgumentParser()
    load_raw_data()