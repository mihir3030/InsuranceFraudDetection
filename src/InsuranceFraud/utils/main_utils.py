import os
from pathlib import Path
import yaml
from InsuranceFraud.logging import logging
from ensure import ensure_annotations
# with help of ConfigBox we can get dictinory keys using dict.key - more refere trails.ipynb
from box import ConfigBox
from box.exceptions import BoxValueError
import json



# ensure_annotation verifies that function output will be -> annotation type output 
# because we mention in annotation type -> ConfigBox type - more refere trails.ipynb
@ensure_annotations
def read_yaml_file(yaml_file_path: Path) -> ConfigBox:
    """reads yaml file and returns yaml file values
    Args:
        path_to_yaml (str): path of input file
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(yaml_file_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml_file lodded from {yaml_file_path}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_of_directories: list, verbose=True):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_of_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"directory created at {path}")

@ensure_annotations
def save_report(report: dict, save_path: str, indentation=4):
    """
    report: reports, save_path: path you want to save
    """
    with open(save_path, "w") as f:
        json.dump(report, f, indent=indentation)
    logging.info(f"json report saved at {save_path}")