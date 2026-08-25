# API

'''
Types of Requests
--------------------
Get -> Read / Select
Post -> Create / Insert / Send
Put -> Update
Delete -> Remove
'''

from fastapi import FastAPI
from app.schema import CardioSchema
from app.model import load_logistic_model
import pandas as pd

# Fast API Objects
app = FastAPI()

model, scaler = load_logistic_model()

# API Endpoints / Requests
@app.get('/')
def home():
    return ('Welcome to the Cardiovascular Disease Prediction')

@app.post('/predict-cardio-logistic')

def predict_cardio(data: CardioSchema):
    input_data = pd.DataFrame([
        # Accept data as JSON Format
        data.model_dump()
    ])

    input_scaler = scaler.transform(input_data)
    prediction = model.predict(input_scaler)[0] # 0 or 1
    return {
        'prediction Status': int(prediction),
        'Status' : 'Likely to be healthy' if prediction == 0 else 'Likely to be unhelthy'
    }




