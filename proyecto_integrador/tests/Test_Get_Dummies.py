import logging
import pandas as pd

# Configurar el manejador de archivo
logging.basicConfig(filename=r'C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\tests\Test_get_dummies.log', 
                    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TestGetDummies:
    def test_get_dummies_columns(self):
        logging.info("Starting test_get_dummies_columns")

        # Create a sample DataFrame
        logging.debug("Creating the sample DataFrame")
        data = {
            "fueltype": ["gas", "diesel", "gas"],
            "aspiration": ["std", "turbo", "std"],
            "doornumber": ["two", "four", "two"],
            "carbody": ["sedan", "hatchback", "sedan"],
            "drivewheel": ["fwd", "rwd", "fwd"],
            "enginetype": ["ohc", "ohcv", "ohc"],
            "cylindernumber": ["four", "six", "four"],
            "fuelsystem": ["mpfi", "mpfi", "mpfi"],
            "CarsRange": ["low", "medium", "high"]
        }
        df = pd.DataFrame(data)
        logging.debug("Sample DataFrame created successfully")

        # Apply get_dummies to the DataFrame
        logging.debug("Applying get_dummies to the DataFrame")
        new_df = pd.get_dummies(columns=["fueltype","aspiration","doornumber","carbody","drivewheel","enginetype",
                                         "cylindernumber","fuelsystem","CarsRange"], data=df)
        logging.debug("get_dummies applied successfully")

        # Check if the dummy columns were created correctly
        logging.debug("Verifying the creation of dummy columns")
        expected_columns = ['fueltype_diesel', 'fueltype_gas', 'aspiration_std', 'aspiration_turbo',
                            'doornumber_four', 'doornumber_two', 'carbody_hatchback', 'carbody_sedan',
                            'drivewheel_fwd', 'drivewheel_rwd', 'enginetype_ohc', 'enginetype_ohcv',
                            'cylindernumber_four', 'cylindernumber_six', 'fuelsystem_mpfi', 'CarsRange_high',
                            'CarsRange_low', 'CarsRange_medium']
        assert set(expected_columns) == set(new_df.columns), "Dummy columns were not created correctly"
        logging.debug("Dummy columns verified successfully")

        logging.info("test_get_dummies_columns completed")

# Crear una instancia de la clase y llamar a la función para ejecutar el código
test = TestGetDummies()
test.test_get_dummies_columns()
