# Predictive-Analysis
## Project Overview
 This project provides a RESTful API to predict machine failures in manufacturing operations based on various process parameters. The API allows users to: </br>

- Upload manufacturing data. </br>
- Train a machine learning model to predict failures.</br>
- Make predictions on new data.</br>

## Dataset
The dataset used is ai4i2020.csv, which contains the following key columns and Descriptions:

- UID:	Unique Identifier</br>
- air_temperature [K]:	Air temperature in Kelvin</br>
- process_temperature [K]:	Process temperature in Kelvin</br>
- rotational_speed [rpm]:	Rotational speed in revolutions per minute (rpm)</br>
- torque [Nm]:	Torque in Newton meters</br>
- tool_wear [min]:	Tool wear in minutes</br>
- machine_failure:	Binary label indicating machine failure (1/0)</br>

## Setup Instructions
### 1. Clone the Repository
git clone https://github.com/yourusername/predictive-analysis.git
`cd predictive-analysis`
### 2. Install Dependencies
Ensure Python (>=3.8) is installed, then install the necessary dependencies:
`pip install -r requirements.txt`
### 3. Run the Application
Start the Flask API by running:
python app/main.py
The API will be available at: `http://127.0.0.1:5000`

#### API Endpoints
1. Upload Data (POST /upload) </br>
Description:
Upload the manufacturing dataset for model training.

Request:
`curl -X POST -F "file=@data/ai4i2020.csv" http://127.0.0.1:5000/upload` </br>
Response (json):
`{
  "message": "File uploaded successfully"
}`

2. Train Model (POST /train) </br>
Description:
Train a logistic regression model on the uploaded dataset.

Request (bash): `curl -X POST http://127.0.0.1:5000/train` </br>
Response (json):
`{
  "accuracy": 0.89
}`

3. Make Predictions (POST /predict) </br>
Description:
Predict machine failure based on input parameters.

Request (bash): </br>

`curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{
    "air_temperature": 300, 
    "process_temperature": 310,
    "rotational_speed": 1500,
    "torque": 40,
    "tool_wear": 50
}'`
</br>

Response (json):

`{
  "Machine_Failure": "Yes",
  "Confidence": 0.87
}`
