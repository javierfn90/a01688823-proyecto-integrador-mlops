# a01688823-proyecto-integrador-mlops
Proyecto Integrador MLOPs

CAR PRICE PREDICTION - KAGGLE DATASET

Dataset Description
The car price prediction dataset available on Kaggle is all about the technical details of various car models. The dataset includes both technical and price details of the cars. The main aim of the dataset is to predict car prices based on given features such as engine power, mileage, manufacturing year, etc.

Problem Addressed
The main problem that this dataset addresses is car price prediction. Given a set of car features like engine power, mileage, manufacturing year, etc., the goal is to predict the car's price. This is a regression task since the car price is a continuous quantity.

Existing Solutions
There are several solutions (notebooks) already developed on Kaggle for this dataset. These solutions include different modeling approaches and techniques like linear regression, random forest regression, support vector regression, etc.

The minimum necessary solution to be able to train and save a model would include:

- Exploratory Data Analysis (EDA)
- Data preprocessing
- Training a regression model
- Model evaluation
- Saving the trained model

Model Scope
The scope of this project is to serve as a proof of concept for car price prediction. While the model will be trained and tested on the Kaggle dataset, the ultimate goal is to demonstrate how data science and machine learning can be applied to real-world problems.

Beyond the solutions already created on Kaggle, several other models can be trained on this dataset. Some of these could include deep learning models like neural networks, or ensemble techniques like boosting.

The final output of this project would be a trained model that can predict a car's price given certain features. This model could be used in an application or a website to predict a car's price in real time.

How to create and activate a virtual environment in windows and linux
Windows
Open the command prompt (cmd) or PowerShell. Make sure you have Python and pip installed. You can check if they are installed by running the commands python --version and pip --version. If they are not installed, you can download them from the official Python website. Install the virtualenv package using the command pip install virtualenv. Create a new virtual environment by running the command virtualenv [environment_name], replacing [environment_name] with the name you want to give to your virtual environment. Activate the virtual environment by running the command [environment_name]\Scripts\activate, replacing [environment_name] with the name you gave to your virtual environment. Once the virtual environment is activated, you can install packages from a requirements.txt file using the command pip install -r requirements.txt. Make sure to specify the correct path to the requirements.txt file.

Linux
Open a terminal window. Make sure you have Python and pip installed. You can check if they are installed by running the commands python3 --version and pip3 --version. If they are not installed, you can install them using your distribution’s package manager (e.g., apt-get install python3 python3-pip on Ubuntu). Install the virtualenv package using the command pip3 install virtualenv. Create a new virtual environment by running the command virtualenv [environment_name], replacing [environment_name] with the name you want to give to your virtual environment. Activate the virtual environment by running the command source [environment_name]/bin/activate, replacing [environment_name] with the name you gave to your virtual environment. Once the virtual environment is activated, you can install packages from a requirements.txt file using the command pip3 install -r requirements.txt. Make sure to specify the correct path to the requirements.txt file.