from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    store_dir_name: Path
    ingested_dir: Path
    split_ratio: Path
    file_name: Path
    training_file_name: Path
    testing_file_name: Path

@dataclass(frozen=True)
class DataPreprocessConfig:
    root_dir: Path
    load_train_file: Path
    load_test_file: Path
    local_file_name: Path
    

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    load_train_file: Path
    local_model_name: Path

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    load_data_file: Path
    load_model_file: Path
    loacl_file_name: Path