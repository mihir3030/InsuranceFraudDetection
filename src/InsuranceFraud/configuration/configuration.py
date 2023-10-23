import os
from pathlib import Path
from InsuranceFraud.logging import logging
from InsuranceFraud.constant import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from InsuranceFraud.utils.main_utils import read_yaml_file, create_directories
from InsuranceFraud.entity.config_entity import DataIngestionConfig, DataPreprocessConfig, ModelTrainerConfig, ModelEvaluationConfig


class ConfigurationManager:
    def __init__(self, config_file=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH) -> None:
        self.config = read_yaml_file(config_file)
        self.params = read_yaml_file(params_file_path)
        create_directories([self.config.artifact_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            store_dir_name=Path(config.store_dir_name),
            ingested_dir=Path(config.ingested_dir),
            split_ratio=config.split_ratio,
            file_name=Path(config.file_name),
            training_file_name=Path(config.training_file_name),
            testing_file_name=Path(config.testing_file_name)
        )

        return data_ingestion_config
    
    def get_data_preprocess_config(self) -> DataPreprocessConfig:
        config = self.config.data_preprocessing
        create_directories([config.root_dir])
        load_train_data_file = os.path.join(self.config.data_ingestion.root_dir, 
                                            self.config.data_ingestion.ingested_dir, 
                                            self.config.data_ingestion.training_file_name)
        load_test_data_file = os.path.join(self.config.data_ingestion.root_dir, 
                                            self.config.data_ingestion.ingested_dir, 
                                            self.config.data_ingestion.testing_file_name)
        
        data_preprocessing_config = DataPreprocessConfig(
            root_dir=Path(config.root_dir),
            load_train_file=Path(load_train_data_file),
            load_test_file=Path(load_test_data_file),
            local_file_name=Path(config.local_file_name)
        )

        return data_preprocessing_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        create_directories([config.root_dir])
        load_train_data = os.path.join(self.config.data_preprocessing.root_dir,
                                       self.config.data_preprocessing.local_file_name)
        
        model_trainer_config = ModelTrainerConfig(
            root_dir=Path(config.root_dir),
            load_train_file=Path(load_train_data),
            local_model_name=Path(config.local_model_name)
        )

        return model_trainer_config
    

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        create_directories([config.root_dir])
        load_model_file = os.path.join(self.config.model_trainer.root_dir,
                                       self.config.model_trainer.local_model_name)
        load_data = os.path.join(self.config.data_preprocessing.root_dir,
                                       self.config.data_preprocessing.local_file_name)
        
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=Path(config.root_dir),
            load_data_file=Path(load_data),
            load_model_file=Path(load_model_file),
            loacl_file_name=Path(config.local_file_name)
        )

        return model_evaluation_config

    