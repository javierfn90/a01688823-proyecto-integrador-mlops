import logging
import pandas as pd

# Configurar el manejador de archivo
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\tests\Test_Data_Existence.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class TestExistence:
    def test_existence(self):
        logger.info("Starting test_existence")

        # Load training data
        logger.debug("Loading training data")
        df_train = pd.read_csv(r'proyecto_integrador\docs\CarPrice_Assignment.csv')

        # Verify training data existence
        if df_train.empty:
            logger.error("No training data")
            assert not df_train.empty, "No training data"
        else:
            logger.info("Training data loaded successfully")

        logger.info("test_existence completed")