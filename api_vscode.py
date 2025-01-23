from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

app = Flask(__name__)
data = None
model = None

@app.route('/upload', methods=['POST'])
def upload():
    global data
    file = request.files['file']
    data = pd.read_csv(file)
    return jsonify({"message": "File uploaded successfully"})

@app.route('/train', methods=['POST'])
def train():
    global model
    X = data[['air_temperature [K]', 'process_temperature [K]', 'rotational_speed [rpm]', 'torque [Nm]', 'tool_wear [min]']]
    y = data['machine_failure']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    joblib.dump(model, 'model.pkl')
    return jsonify({"accuracy": accuracy})

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.get_json()
    loaded_model = joblib.load('model.pkl')
    prediction = loaded_model.predict([[input_data['air_temperature'], input_data['process_temperature'], input_data['rotational_speed'], input_data['torque'], input_data['tool_wear']]])
    confidence = loaded_model.predict_proba([[input_data['air_temperature'], input_data['process_temperature'], input_data['rotational_speed'], input_data['torque'], input_data['tool_wear']]])[0].max()
    result = "Yes" if prediction[0] == 1 else "No"
    return jsonify({"Machine_Failure": result, "Confidence": confidence})

if __name__ == '__main__':
    app.run(debug=True)
