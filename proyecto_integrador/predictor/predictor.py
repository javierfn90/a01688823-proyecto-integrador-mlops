import argparse
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import logging

# Configure logging
logging.basicConfig(filename=r'C:\\Users\\francisco.figueroa\\a01688823-proyecto-integrador-mlops\\proyecto_integrador\\predictor\\predictor.log', 
                    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class ModelPredictor:
    """
    A class to load a trained machine learning model and make predictions on new data.

    Parameters:
        model_path (str): Path to the trained model file (joblib format).

    Methods:
        predict(new_data):
            Makes predictions on the provided new_data using the loaded model.

    Usage:
        $ python predictor.py 
        C:\\Users\\francisco.figueroa\\a01688823-proyecto-integrador-mlops\\proyecto_integrador\\models\\model_AdaBoostRegressor.pkl 
        C:\\Users\\francisco.figueroa\\a01688823-proyecto-integrador-mlops\\proyecto_integrador\\preprocess\\preprocessed_data.csv
    """

    def __init__(self, model_path):
        """
        Initializes the ModelPredictor instance.

        Parameters:
            model_path (str): Path to the trained model file (joblib format).
        """
        self.model = joblib.load(model_path)
        logging.info(f"Loaded model from {model_path}")

    def predict(self, new_data):
        """
        Makes predictions on the provided new_data using the loaded model.

        Parameters:
            new_data: The data on which to make predictions.

        Returns:
            Predicted outputs from the model.
        """
        logging.info("Making predictions")
        return self.model.predict(new_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Model Predictor')
    parser.add_argument('model_path', type=str, help='Path to the trained model file')
    parser.add_argument('new_data', type=str, help='Path to the file containing new data for prediction')
    args = parser.parse_args()

    predictor = ModelPredictor(args.model_path)
    logging.info("Model Predictor initialized")

    new_data = pd.read_csv(args.new_data)
    logging.info(f"Loaded new data from {args.new_data}")

    predictions = predictor.predict(new_data)
    logging.debug("Predictions made")

    print(predictions)
