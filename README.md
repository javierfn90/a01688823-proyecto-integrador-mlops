# a01688823-proyecto-integrador-mlops
* Contact: Javier Figueroa
* E-mail: javierfn90@hotmail.com

# Proyecto Integrador MLOPs

# CAR PRICE PREDICTION - KAGGLE DATASET

## Dataset Description
The car price prediction dataset available on Kaggle is all about the technical details of various car models. The dataset includes both technical and price details of the cars. The main aim of the dataset is to predict car prices based on given features such as engine power, mileage, manufacturing year, etc.

## Problem Addressed
The main problem that this dataset addresses is car price prediction. Given a set of car features like engine power, mileage, manufacturing year, etc., the goal is to predict the car's price. This is a regression task since the car price is a continuous quantity.

## Existing Solutions
There are several solutions (notebooks) already developed on Kaggle for this dataset. These solutions include different modeling approaches and techniques like linear regression, random forest regression, support vector regression, etc.

The minimum necessary solution to be able to train and save a model would include:

- Exploratory Data Analysis (EDA)
- Data preprocessing
- Training a regression model
- Model evaluation
- Saving the trained model

## Model Scope
The scope of this project is to serve as a proof of concept for car price prediction. While the model will be trained and tested on the Kaggle dataset, the ultimate goal is to demonstrate how data science and machine learning can be applied to real-world problems.

Beyond the solutions already created on Kaggle, several other models can be trained on this dataset. Some of these could include deep learning models like neural networks, or ensemble techniques like boosting.

The final output of this project would be a trained model that can predict a car's price given certain features. This model could be used in an application or a website to predict a car's price in real time.


## How to create and activate a virtual environment in windows and linux

* Windows:

Open the command prompt (cmd) or PowerShell. Make sure you have Python and pip installed. You can check if they are installed by running the commands 

```bash
 python --version and pip --version
```

If they are not installed, you can download them from the official Python website. Install the virtualenv package using the command:

```bash
 pip install virtualenv
```

 Create a new virtual environment by running the command:

 ```bash
 py -3.10 -m venv [environment_name]
```

Activate the virtual environment by running the command 

 ```bash
 . .\[environment_name]\Scripts\activate
```

Once the virtual environment is activated, you can install packages from a requirements.txt file using the command 

 ```bash
 pip install -r requirements.txt
```

# Docker Compose

## Build Docker image individually

* Run next command to build de docker image with the app.

```bash
 docker build -t proyecto_integrador .
```

* Inspect the image created by running this command:

```bash
 docker images
```

* Then, run this comand to run the image in a container.

```bash
bash docker run -d --rm --name proyecto_integrador-container -p 3000:8000 proyecto_integrador
```

* Check the container running
```bash
docker ps -a
```

* Debug container
```bash
docker exec -it ID_CONTAINER /bin/bash
```

* Delete all images

```bash
docker rmi -f $(docker images -aq)
```

* Delete all containers

```bash
docker rm -f $(docker ps -aq)  
```

## Create the network

First, create the network AIService by running this command:

```bash
docker network create AIservice
```

## Run Docker Compose

* Create a file named docker-compose.yml in the root folder of your project. This file will contain the configuration for the frontend and API services.

* Open the docker-compose.yml file in a text editor and add the following content:

```bash
version: '3'
services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - 3000:3000
  api:
    build:
      context: ./api
      dockerfile: Dockerfile
    ports:
      - 8000:8000
```

* Create the frontend and api folders in the same location as the docker-compose.yml file. Each folder should contain the necessary files and structure for the frontend and API, including the respective Dockerfile and requirements files.

* Be sure you are in the directory where the docker-compose.yml file is located

* Run next command to start the Server and Frontend APIs

```bash
docker-compose up --build
```

* Once the containers are running, you can access the frontend at http://localhost:3000 and the API at http://localhost:8000.

## Test request

### CURL request

* For Frontend

```bash
docker exec CONTAINER_ID curl -X GET http://localhost:3000/
```

* For Frontend

```bash
docker exec CONTAINER_ID curl -X GET http://localhost:8000/
```

# Check logs

```bash
docker logs -f ID_CONTAINER | Select-String -Pattern "Debug" 
```

## Extract logs

* To extract the logs, you can copy them to your local machine by running this command. 

```bash
docker cp CONTAINER_ID:/app/server.log . 
```