import logging
import logging.handlers
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a file handler for the log file
file_handler = logging.handlers.RotatingFileHandler(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\train\train.log', 
                                                    maxBytes=1024*1024, backupCount=5)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Add the file handler to the logger
logging.getLogger('').addHandler(file_handler)

# Load the dataset
logging.info("Loading the dataset")
df = pd.read_csv(r'proyecto_integrador\preprocess\preprocessed_data.csv')

# Train-test split
logging.info("Performing train-test split")
x = df.drop(columns=["price"])
y = df["price"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Model training
training_score = []
testing_score = []

def model_prediction(model):
    logging.info(f"Training {model.__class__.__name__} model")
    model.fit(x_train, y_train)
    x_train_pred = model.predict(x_train)
    x_test_pred = model.predict(x_test)
    a = r2_score(y_train, x_train_pred) * 100
    b = r2_score(y_test, x_test_pred) * 100
    training_score.append(a)
    testing_score.append(b)

# Models evaluation

# Linear Regression
logging.info("Evaluating Linear Regression model")
model_prediction(LinearRegression())
# Save the model
logging.info("Saving Linear Regression model")
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_LinearRegression.pkl')

# Decision Tree
logging.info("Evaluating Decision Tree model")
model_prediction(DecisionTreeRegressor())
# Save the model
logging.info("Saving Decision Tree model")
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_DecisionTreeRegressor.pkl')

# Random Forest
logging.info("Evaluating Random Forest model")
model_prediction(RandomForestRegressor())
# Save the model
logging.info("Saving Random Forest model")
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_RandomForestRegressor.pkl')

# Ada Boost
logging.info("Evaluating Ada Boost model")
model_prediction(AdaBoostRegressor())
# Save the model
logging.info("Saving Ada Boost model")
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_AdaBoostRegressor.pkl')

# Gradient Boosting
logging.info("Evaluating Gradient Boosting model")
model_prediction(GradientBoostingRegressor())
# Save the model
logging.info("Saving Gradient Boosting model")
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_GradientBoostingRegressor.pkl')

# LGBM
logging.info("Evaluating LGBM model")
model_prediction(LGBMRegressor())
# Save the model
logging.info("Saving LGBM model")
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_LGBMRegressor.pkl')

# XGB
logging.info("Evaluating XGB model")
model_prediction(XGBRegressor())
# Save the model
logging.info("Saving XGB model")
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_XGBRegressor.pkl')

# Cat Boost
logging.info("Evaluating Cat Boost model")
model_prediction(CatBoostRegressor(verbose=False))
# Save the model
logging.info("Saving Cat Boost model")
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_CatBoostRegressor.pkl')