import logging
import requests
import shutil

# Set up logging configuration
logging.basicConfig(filename='proyecto_integrador/load/load.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create logger
logger = logging.getLogger(__name__)

# Add file handler to logger
file_handler = logging.FileHandler('proyecto_integrador\load\load.log')
file_handler.setLevel(logging.DEBUG)

# Create formatter and add it to the file handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# URL of the file to download
file_url = "https://www.kaggle.com/datasets/hellbuoy/car-price-prediction/download?datasetVersionNumber=1"

# Destination path for the downloaded file
file_destination = r"C:\Users\francisco.figueroa\a01688823-proyecto-integrador-mlops\proyecto_integrador\data\CarPrice_Assignment.csv"

# Send a GET request to the file URL
response = requests.get(file_url, stream=True)

# Check if the request was successful
if response.status_code == 200:
    # Open the file destination in binary mode
    with open(file_destination, "wb") as file:
        # Iterate over the response content in chunks and write to the file
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)

    logger.info("File downloaded successfully.")
else:
    logger.error("Failed to download the file.")
    logger.warning("Check the file URL or internet connection.")