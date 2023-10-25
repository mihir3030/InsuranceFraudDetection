from InsuranceFraud.pipeline.training_pipeline import training_pipeline
from InsuranceFraud.logging import logging

if __name__ == '__main__':
    try:
        logging.info("Training pipeline started")
        training_pipeline()
    except Exception as e:
        logging.exception(e)
        logging.info(f">>>>>>>>>>>>>>>>>> Training Pipeline Failed\n\n X========================X\n\n")
        raise e