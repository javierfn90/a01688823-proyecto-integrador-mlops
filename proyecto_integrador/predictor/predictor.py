import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Load the preprocessed data
data = pd.read_csv('proyecto_integrador\preprocess\preprocessed_data.csv')

# Load the trained models
model_abr = joblib.load(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_AdaBoostRegressor.pkl')
model_cbr = joblib.load(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_CatBoostRegressor.pkl')
model_dtr = joblib.load(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_DecisionTreeRegressor.pkl')
model_gbr = joblib.load(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_GradientBoostingRegressor.pkl')
model_lgbm = joblib.load(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_LGBMRegressor.pkl')
model_lr = joblib.load(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_LinearRegression.pkl')
model_rf = joblib.load(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_RandomForestRegressor.pkl')
model_xgb = joblib.load(r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\models\model_XGBRegressor.pkl')

# Make predictions with each model
predictions_abr = model_abr.predict(data)
predictions_cbr = model_cbr.predict(data)
predictions_dtr = model_dtr.predict(data)
predictions_gbr = model_gbr.predict(data)
predictions_lgbm = model_lgbm.predict(data)
predictions_lr = model_lr.predict(data)
predictions_rf = model_rf.predict(data)
predictions_xgb = model_xgb.predict(data)

# Create a DataFrame for each model's predictions
predictions_abr_df = pd.DataFrame(predictions_abr, columns=['prediction_abr'])
predictions_cbr_df = pd.DataFrame(predictions_cbr, columns=['prediction_cbr'])
predictions_dtr_df = pd.DataFrame(predictions_dtr, columns=['prediction_dtr'])
predictions_gbr_df = pd.DataFrame(predictions_gbr, columns=['prediction_gbr'])
predictions_lgbm_df = pd.DataFrame(predictions_lgbm, columns=['prediction_lgbm'])
predictions_lr_df = pd.DataFrame(predictions_lr, columns=['prediction_lr'])
predictions_rf_df = pd.DataFrame(predictions_rf, columns=['prediction_rf'])
predictions_xgb_df = pd.DataFrame(predictions_xgb, columns=['prediction_xgb'])

# Concatenate the individual DataFrames into a single DataFrame
all_predictions_df = pd.concat([predictions_abr_df, predictions_cbr_df,
                                predictions_dtr_df, predictions_gbr_df,
                                predictions_lgbm_df, predictions_lr_df,
                                predictions_rf_df, predictions_xgb_df], axis=1)
    
# Save the predictions to a file
all_predictions_df.to_csv('all_predictions.csv', index=False)
