# Import the necessary libraries
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

# Load the dataset
df = pd.read_csv(r'proyecto_integrador\preprocess\preprocessed_data.csv')

# Train-test split
x = df.drop(columns=["price"])
y = df["price"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# Model training
training_score = []
testing_score = []

def model_prediction(model):
    model.fit(x_train, y_train)
    x_train_pred = model.predict(x_train)
    x_test_pred = model.predict(x_test)
    a = r2_score(y_train, x_train_pred) * 100
    b = r2_score(y_test, x_test_pred) * 100
    training_score.append(a)
    testing_score.append(b)

# Models evaluation

#Linear Regression
model_prediction(LinearRegression())
# Save the model
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_LinearRegression.pkl')

#Decission Tree
model_prediction(DecisionTreeRegressor())
# Save the model
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_DecisionTreeRegressor.pkl')

#Random Forest
model_prediction(RandomForestRegressor())
# Save the model
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_RandomForestRegressor.pkl')

#Ada Boost
model_prediction(AdaBoostRegressor())
# Save the model
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_AdaBoostRegressor.pkl')

#Gradient Boosting
model_prediction(GradientBoostingRegressor())
# Save the model
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_GradientBoostingRegressor.pkl')

#LGBM
model_prediction(LGBMRegressor())
# Save the model
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_LGBMRegressor.pkl')

#XGB
model_prediction(XGBRegressor())
# Save the model
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_XGBRegressor.pkl')

#Cat Boost
model_prediction(CatBoostRegressor(verbose=False))
# Save the model
joblib.dump(model_prediction, r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_CatBoostRegressor.pkl')