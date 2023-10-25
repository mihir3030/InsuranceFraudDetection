import os
import pandas as pd
from InsuranceFraud.logging import logging
from InsuranceFraud.entity.config_entity import DataPreprocessConfig

class DataPreprocessing:
    def __init__(self, data_preprocessing_config: DataPreprocessConfig) -> None:
        self.data_preprocessing_config = data_preprocessing_config

    def read_data(self) -> pd.DataFrame:
        training_file = self.data_preprocessing_config.load_train_file
        dataframe = pd.read_csv(training_file)
        logging.info(f"read data from {training_file} successufully")
        
        # dropping columns which are not necessary for prediction
        to_drop = ['policy_number','policy_bind_date','policy_state','insured_zip','incident_location','incident_date',
                'incident_state','incident_city','insured_hobbies','auto_make','auto_model','auto_year']

        dataframe.drop(to_drop, axis=1, inplace=True)
        # dropping columns from our heatmap
        dataframe.drop(['age', 'total_claim_amount'], axis=1, inplace=True)
        logging.info(f"dropped unwanted columns completed")


        # handling missing values
        dataframe['property_damage'] = dataframe['property_damage'].fillna(dataframe['property_damage'].mode()[0])
        dataframe['police_report_available'] = dataframe['police_report_available'].fillna(dataframe['police_report_available'].mode()[0])
        dataframe['collision_type'] = dataframe['collision_type'].fillna(dataframe['collision_type'].mode()[0])
        logging.info(f"handled missing values in our dataset completed")

        dataframe['fraud_reported'] = dataframe['fraud_reported'].replace({'N':0, 'Y':1})        
        # handling categorical data
        dataframe = pd.get_dummies(dataframe, drop_first=True, dtype=int)
        logging.info(f"categorical columns converted into numerical successfully")
        # print(dataframe.shape)

        root_dir = self.data_preprocessing_config.root_dir
        local_file_name = self.data_preprocessing_config.local_file_name
        local_file_path = os.path.join(root_dir, local_file_name)

        dataframe.to_csv(local_file_path, index=False)
        logging.info(f"preprocess data save at {local_file_path}")