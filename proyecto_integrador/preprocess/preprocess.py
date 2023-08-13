import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the data
df = pd.read_csv(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\data\CarPrice_Assignment.csv')

# Perform preprocessing steps

# Create a new DataFrame with all the useful features
new_df = df[['fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel', 'enginetype', 'cylindernumber',
             'fuelsystem', 'wheelbase', 'carlength', 'carwidth', 'curbweight', 'enginesize', 'boreratio',
             'horsepower', 'citympg', 'highwaympg', 'price']]

# Create dummy variables for all the categorical features
new_df = pd.get_dummies(new_df, columns=["fueltype", "aspiration", "doornumber", "carbody", "drivewheel",
                                         "enginetype", "cylindernumber", "fuelsystem"])

# Feature scaling of numerical data
scaler = StandardScaler()
num_cols = ['wheelbase', 'carlength', 'carwidth', 'curbweight', 'enginesize', 'boreratio', 'horsepower',
            'citympg', 'highwaympg']

new_df[num_cols] = scaler.fit_transform(new_df[num_cols])

# Save the preprocessed data
new_df.to_csv(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\preprocess\preprocessed_data.csv', index=False)