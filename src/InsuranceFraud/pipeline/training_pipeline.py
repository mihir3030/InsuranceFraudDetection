import os
from InsuranceFraud.logging import logging
from InsuranceFraud.configuration.configuration import ConfigurationManager
from InsuranceFraud.components.data_ingestion import DataIngestion
from InsuranceFraud.components.data_preprocessing import DataPreprocessing
from InsuranceFraud.components.model_trainer import ModelTrainer
from InsuranceFraud.components.model_evaluation import ModelEvaluation


def training_pipeline():
    configuration_manager = ConfigurationManager()
    data_ingestion_config = configuration_manager.get_data_ingestion_config()
    data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
    data_ingestion.export_data_into_feature_store()
    data_ingestion.split_data_as_train_test_split()

    data_preprocessing_config = configuration_manager.get_data_preprocess_config()
    data_preprocessing = DataPreprocessing(data_preprocessing_config)
    data_preprocessing.read_data()

    # training
    model_trainer_config = configuration_manager.get_model_trainer_config()
    model_trainer = ModelTrainer(model_trainer_config)
    model_trainer.read_data()
    model_trainer.trainer()

    #evaluation
    model_evaluation_config = configuration_manager.get_model_evaluation_config()
    model_evaluation = ModelEvaluation(model_evaluation_config)
    model_evaluation.read_data()
    model_evaluation.model_metrics()
    model_evaluation.save_report()

if __name__ == "__main__":
    try:
        logging.info(f">>>>>>>>>started")
        training_pipeline()
        logging.info(f">>>>>>>>>>compleated successfully\n\n X==========================X\n\n")
    except Exception as e:
        logging.exception(e)
        raise e