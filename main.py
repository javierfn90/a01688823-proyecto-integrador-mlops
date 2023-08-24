import os
import sys
from pydantic import BaseModel
from fastapi import FastAPI
from proyecto_integrador.predictor.predictor import ModelPredictor
from proyecto_integrador.load.load import DataLoader
from starlette.responses import JSONResponse

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

class InputData(BaseModel):
    feature1: float
    feature2: float
    # Add more features as needed

class OutputData(BaseModel):
    prediction: int

#add FastAPI to the project
app = FastAPI()

@app.post("/train")
def train_model():
    # Implement the logic to train a new model
    # Return a response indicating the success or failure of the training process
    pass

@app.post("/predict", response_model=OutputData)
def predict(input_data: InputData):
    # Convert the input data to a numpy array
    input_array = np.array([[input_data.feature1, input_data.feature2]])

    # Make predictions using the loaded model
    prediction = model.predict(input_array)

    # Create an instance of the output data model and return it
    output_data = OutputData(prediction=int(prediction[0]))
    return output_data