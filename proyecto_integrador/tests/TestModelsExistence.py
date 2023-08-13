import os


class TestModelsExistence:
    def __init__(self, model_names):
        self.model_names = model_names

    def verify_saved_model(self):
        for model_names in self.model_names:
            if os.path.exists(model_names):
                print(f"{model_names} exist.")
            else:
                print(f"{model_names} has not been found.")


models = TestModelsExistence(
    [
        r'proyecto_integrador\models\model_AdaBoostRegressor.pkl',
        r'proyecto_integrador\models\model_CatBoostRegressor.pkl',
        r'proyecto_integrador\models\model_DecisionTreeRegressor.pkl',
        r'proyecto_integrador\models\model_GradientBoostingRegressor.pkl',
        r'proyecto_integrador\models\model_LGBMRegressor.pkl',
        r'proyecto_integrador\models\model_LinearRegression.pkl',
        r'proyecto_integrador\models\model_RandomForestRegressor.pkl',
        r'proyecto_integrador\models\model_XGBRegressor.pkl'])

models.verify_saved_model()
