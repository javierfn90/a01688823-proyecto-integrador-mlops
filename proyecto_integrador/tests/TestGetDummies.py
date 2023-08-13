import pandas as pd

def test_get_dummies():
    # Create a sample DataFrame
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

    # Apply get_dummies to the DataFrame
    new_df = pd.get_dummies(columns=["fueltype","aspiration","doornumber","carbody","drivewheel","enginetype",
                                     "cylindernumber","fuelsystem","CarsRange"], data=df)

    # Check if the dummy columns were created correctly
    expected_columns = ['fueltype_diesel', 'fueltype_gas', 'aspiration_std', 'aspiration_turbo',
                        'doornumber_four', 'doornumber_two', 'carbody_hatchback', 'carbody_sedan',
                        'drivewheel_fwd', 'drivewheel_rwd', 'enginetype_ohc', 'enginetype_ohcv',
                        'cylindernumber_four', 'cylindernumber_six', 'fuelsystem_mpfi', 'CarsRange_high',
                        'CarsRange_low', 'CarsRange_medium']
    assert set(expected_columns) == set(new_df.columns), "Dummy columns were not created correctly"

    print("Test successful")

# Run the test function
test_get_dummies()