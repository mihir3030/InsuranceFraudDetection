import os
import pandas as pd
from InsuranceFraud.logging import logging
from sklearn.model_selection import train_test_split
from InsuranceFraud.utils.main_utils import create_directories
from InsuranceFraud.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig) -> None:
        self.data_ingestion_config = data_ingestion_config

    def export_data_into_feature_store(self) -> pd.DataFrame:
        """
        Export data from cloud as DataFrame into Feature store
        """
        self.datframe = pd.read_csv("research/insuranceFraud.csv")

        data_ingestion_root_dir = self.data_ingestion_config.root_dir
        feature_store_dir = self.data_ingestion_config.store_dir_name
        feature_store_path = os.path.join(data_ingestion_root_dir, feature_store_dir)
        create_directories([feature_store_path])

        feature_store_file = self.data_ingestion_config.file_name
        feature_store_file_path = os.path.join(feature_store_path, feature_store_file,)
        print(feature_store_file_path)
        self.datframe.to_csv(feature_store_file_path, index=False)
        

    def split_data_as_train_test_split(self) -> None:
        train_set, test_set = train_test_split(
            self.datframe, test_size=self.data_ingestion_config.split_ratio
        )
        logging.info(f"Performed data split into train and test")
        
        root_dir = self.data_ingestion_config.root_dir
        ingested_dir = self.data_ingestion_config.ingested_dir
        ingested_dir_path = os.path.join(root_dir, ingested_dir)
        create_directories([ingested_dir_path])

        train_set_path = os.path.join(ingested_dir_path, self.data_ingestion_config.training_file_name)
        train_set.to_csv(train_set_path,  index=False)
        
        test_set_path = os.path.join(ingested_dir_path, self.data_ingestion_config.testing_file_name)
        test_set.to_csv(test_set_path, index=False)

    def initiate_data_ingestion(self):
        pass

