Anisha-20110-pset2
==============================

assignment 2 ML-Ops

Project Organization
------------

    ├── Artifacts               <- Contains genrated trained model's .pkl files
    ├── Makefile                <- Makefile with commands like `make data` or `make train`
    ├── README.md               <- The top-level README for developers using this project.
    ├── data
    │   ├── external            <- Data from third party sources.
    │   ├── processed           <- The final, canonical data sets for modeling.
    │   └── raw                 <- The original, immutable data dump.
    ├── models                  <- Trained and serialized models, model predictions, or model summaries
    │
    ├── requirements.txt        <- The requirements file for reproducing the analysis environment, e.g.
    │                             generated with `pip freeze > requirements.txt`
    ├── setup.py                <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                     <- Source code for use in this project.
    │   ├── __init__.py         <- Makes src a Python module
    │   │
    │   ├── data                <- Scripts to download or generate data
    │   │   └── load_and_process_data.py
    │   │
    │   ├── models              <- Scripts to train models and then use trained models to make
    │       │                       predictions
    │       └── train_model.py  <- To train model: python3 src/models/train_model.py
    │   
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.

Inorder to run the model, you will need to set your mlflow and dagshub credentials

    dvc remote modify origin --local auth basic
    dvc remote modify origin --local user <DAGSHUB_ID>
    dvc remote modify origin --local password <DAGSHUB_TOKEN>

    export MLFLOW_TRACKING_USERNAME=<DAGSHUB_ID>
    export MLFLOW_TRACKING_PASSWORD=<DAGSHUB_TOKEN>
    

# Links:
    DagsHub: https://dagshub.com/anibhush/Anisha-20110-pset2
    https://dagshub.com/anibhush/Anisha-20110-pset2/experiments/#/
    
    
# Data Flow Pipeline:
<img width="1636" alt="image" src="https://user-images.githubusercontent.com/32108645/177392591-d6331985-520d-4e5f-bc68-5fbee58fc423.png">


# ML Flow:
<img width="1368" alt="image" src="https://user-images.githubusercontent.com/32108645/177392741-f32f72fe-202c-4674-b9ca-e203a5ccc0f4.png">
