import logging
import os

# Configurar el manejador de archivo
logging.basicConfig(filename=r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\tests\Test_models_existence.log', 
                    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TestExistence:
    def __init__(self, model_names):
        self.model_names = model_names

    def test_saved_model_existence(self):
        logging.info("Starting test_saved_model_existence")

        for model_name in self.model_names:
            logging.debug(f"Checking existence of model: {model_name}")
            assert os.path.exists(model_name), f"{model_name} has not been found."
            logging.debug(f"Model {model_name} exists")

        logging.info("test_saved_model_existence completed")

# Inicializar los nombres de los modelos y crear una instancia de TestExistence
model_names = [
    r'proyecto_integrador\models\model_AdaBoostRegressor.pkl',
    r'proyecto_integrador\models\model_CatBoostRegressor.pkl',
    r'proyecto_integrador\models\model_DecisionTreeRegressor.pkl',
    r'proyecto_integrador\models\model_GradientBoostingRegressor.pkl',
    r'proyecto_integrador\models\model_LGBMRegressor.pkl',
    r'proyecto_integrador\models\model_LinearRegression.pkl',
    r'proyecto_integrador\models\model_RandomForestRegressor.pkl',
    r'proyecto_integrador\models\model_XGBRegressor.pkl'
]

models = TestExistence(model_names)

# Llamar al método para ejecutar el código
models.test_saved_model_existence()