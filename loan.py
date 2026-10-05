from flask import Flask
from flask import request
import pickle

app = Flask(__name__)

with open("classifier.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "<h1>Loan Application</h1><p>Welcome to the Loan Application!</p>"


@app.route('/predict', methods=['POST'])
def make_prediction():
    data = request.get_json()  # Get the JSON data from the request
    # print(f"Received data for prediction: {data}")  # Log the received data
    # Here you would typically process the input data and make a prediction
    if data['Gender'] == 'Male':
        gender = 0
    else:
        gender = 1

    if data['Married'] == "No":
        married = 0
    else:
        married = 1

    input_features = [[gender, married, data['ApplicantIncome'], data['LoanAmount'], data['Credit_History']]]
    prediction = model.predict(input_features)
    if prediction[0] == 1:
        return {"prediction": "Loan Approved"}
    else:
        return {"prediction": "Loan Rejected"}

    # return {"prediction": prediction.tolist()}


@app.route('/predict', methods=['GET'])
def get_predict():
    return {"message": "Prediction results will be displayed here."}


if __name__ == "__main__":
    app.run(debug=True)