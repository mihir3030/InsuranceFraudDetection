import os
import pandas as pd
from sklearn.metrics import f1_score
from InsuranceFraud.logging import logging
from InsuranceFraud.entity.config_entity import ModelEvaluationConfig
from InsuranceFraud.utils.main_utils import save_report
import joblib


class ModelEvaluation:
    def __init__(self, model_evaluation_config: ModelEvaluationConfig) -> None:
        self.model_evaluation_config = model_evaluation_config

    def read_data(self) -> pd.DataFrame:
        data_path = self.model_evaluation_config.load_data_file
        dataframe = pd.read_csv(data_path)
        self.x = dataframe.drop(['fraud_reported'], axis=1)
        self.y = dataframe['fraud_reported']

    def model_metrics(self):
        model = joblib.load(self.model_evaluation_config.load_model_file)
        y_pred = model.predict(self.x)
        self.f1_score = f1_score(self.y, y_pred)

    def save_report(self):
        scores = {
            "f1_score": self.f1_score
        }
        
        root_dir = self.model_evaluation_config.root_dir
        report_file = self.model_evaluation_config.loacl_file_name
        report_file_path = os.path.join(root_dir, report_file)

        save_report(scores, report_file_path)
