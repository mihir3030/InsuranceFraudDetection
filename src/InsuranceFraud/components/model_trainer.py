import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from InsuranceFraud.logging import logging
from InsuranceFraud.entity.config_entity import ModelTrainerConfig
import joblib



class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig) -> None:
        self.model_trainer_config = model_trainer_config

    def read_data(self) -> pd.DataFrame:
        data_path = self.model_trainer_config.load_train_file
        self.dataframe = pd.read_csv(data_path)

    def trainer(self):
        x = self.dataframe.drop(['fraud_reported'], axis=1)
        y = self.dataframe['fraud_reported']
        model = RandomForestClassifier()
        model.fit(x, y)
        print(model.score(x, y))
        logging.info(model.score(x, y))
        
        root_dir = self.model_trainer_config.root_dir
        model_file = self.model_trainer_config.local_model_name
        model_file_path = os.path.join(root_dir, model_file)

        joblib.dump(model, model_file_path)
