import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging

# Configure logging
logging.basicConfig(filename=r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\preprocess\preprocessing.log', 
                    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the data
logging.info('Loading the data')
try:
    df = pd.read_csv(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\data\CarPrice_Assignment.csv')
    logging.debug('Data loaded successfully')
except Exception as e:
    logging.error(f'Error loading the data: {str(e)}')

# Perform preprocessing steps

# Create a new DataFrame with all the useful features
logging.info('Creating new DataFrame with useful features')
try:
    new_df = df[['fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel', 'enginetype', 'cylindernumber',
                 'fuelsystem', 'wheelbase', 'carlength', 'carwidth', 'curbweight', 'enginesize', 'boreratio',
                 'horsepower', 'citympg', 'highwaympg', 'price']]
    logging.debug('New DataFrame created successfully')
except Exception as e:
    logging.error(f'Error creating new DataFrame: {str(e)}')

# Create dummy variables for all the categorical features
logging.info('Creating dummy variables for categorical features')
try:
    new_df = pd.get_dummies(new_df, columns=["fueltype", "aspiration", "doornumber", "carbody", "drivewheel",
                                             "enginetype", "cylindernumber", "fuelsystem"])
    logging.debug('Dummy variables created successfully')
except Exception as e:
    logging.error(f'Error creating dummy variables: {str(e)}')

# Feature scaling of numerical data
logging.info('Performing feature scaling')
try:
    scaler = StandardScaler()
    num_cols = ['wheelbase', 'carlength', 'carwidth', 'curbweight', 'enginesize', 'boreratio', 'horsepower',
                'citympg', 'highwaympg']
    new_df[num_cols] = scaler.fit_transform(new_df[num_cols])
    logging.debug('Feature scaling performed successfully')
except Exception as e:
    logging.error(f'Error performing feature scaling: {str(e)}')

# Save the preprocessed data
logging.info('Saving the preprocessed data')
try:
    new_df.to_csv(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\preprocess\preprocessed_data.csv', index=False)
    logging.debug('Preprocessed data saved successfully')
except Exception as e:
    logging.error(f'Error saving the preprocessed data: {str(e)}')