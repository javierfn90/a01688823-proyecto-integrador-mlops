import requests
import shutil

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

    print("File downloaded successfully.")
else:
    print("Failed to download the file.")