import logging
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def test_scaler_scaling():
    logging.info("Starting test_scaler_scaling")

    # Create a sample DataFrame
    logging.debug("Creating sample DataFrame")
    data = {
        "wheelbase": [100, 110, 120],
        "carlength": [150, 160, 170],
        "carwidth": [50, 60, 70],
        "curbweight": [2000, 2100, 2200],
        "enginesize": [1000, 1100, 1200],
        "boreratio": [1.0, 1.1, 1.2],
        "horsepower": [100, 110, 120],
        "citympg": [20, 25, 30],
        "highwaympg": [30, 35, 40]
    }
    df = pd.DataFrame(data)

    # Apply StandardScaler to the numerical columns
    logging.debug("Applying StandardScaler")
    num_cols = ['wheelbase', 'carlength', 'carwidth', 'curbweight', 'enginesize', 'boreratio', 'horsepower',
                'citympg', 'highwaympg']
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

    # Check if the numerical columns were scaled correctly
    logging.debug("Checking scaling results")
    expected_mean = np.zeros(len(num_cols))
    expected_std = np.ones(len(num_cols))
    for col in num_cols:
        assert np.allclose(df[col].mean(), expected_mean), f"Mean of column {col} is not correct"
        assert np.allclose(df[col].std(ddof=0), expected_std), f"Standard deviation of column {col} is not correct"
    logging.debug("Scaling results are correct")

    logging.info("test_scaler_scaling completed")


# Configure logging and call the function
if __name__ == "__main__":
    logging.basicConfig(filename=r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\tests\Test_scaler.log', 
                        level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    test_scaler_scaling()