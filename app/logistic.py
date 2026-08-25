import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests


from models.model import logistic_cardio_predict

st.header('Logistic Page')



features, scaler, model, Y_pred, cr, cm =logistic_cardio_predict()

API_URL = 'https://cardiovasculardisease-utej.onrender.com/predict_cardio'

age = st.sidebar.slider(
    'Age',
    max_value = 70,
    min_value = 21,
    value = 60,
    step = 1
)

gender_dict = {1: "Female", 2: "Male"}
# gender = st.sidebar.radio(
#     'Gender',
#     # get key
#     options=list(gender_dict.keys()),
#     # get values
#     format_func=lambda x: gender_dict.get(x)
# )


gender = st.sidebar.selectbox(
    'Gender',
    options = list(gender_dict.keys()),
    format_func=lambda x: gender_dict.get(x)
)

height = st.sidebar.slider(
    'Height',
    max_value = 200,
    min_value = 136,
    value = 145,
    step = 1
)

weight = st.sidebar.slider(
    'Weight',
    max_value = 120,
    min_value = 35,
    value = 60,
    step = 1
)


ap_hi = st.sidebar.slider(
    'Systolic Pressure',
    max_value = 200,
    min_value = 90,
    value = 120,
    step = 1
)
ap_lo = st.sidebar.slider(
    'Disystolic Pressure',
    max_value = 100,
    min_value = 50,
    value = 80,
    step = 1
)
cholesterol_dict = {1: "Low Cholesterol",2: "Mild Cholesterol", 3: "High Cholesterol"}
cholestrol = st.sidebar.selectbox(
    'Cholesterol',
    options = list(cholesterol_dict.keys()),
    format_func=lambda x: cholesterol_dict.get(x)
)

gluc_dict = {1: "Low Glucose",2: "Mild Glucose", 3: "High Glucose"}

gluc = st.sidebar.selectbox(
    'Glucose',
    options = list(gluc_dict.keys()),
    format_func=lambda x: gluc_dict.get(x)
)

smoke_dict = {0: "Non-Smoker", 1: "Smoker"}
smoke = st.sidebar.selectbox(
    'Smoker',
    options = list(smoke_dict.keys()),
    format_func=lambda x: smoke_dict.get(x)
)

alco_dict = {0: "Non-Alcoholic", 1: "Alcoholic"}
alco = st.sidebar.selectbox(
    'Alcoholic',
    options = list(alco_dict.keys()),
    format_func=lambda x: alco_dict.get(x)
)

active_dict = {0: "Inactive", 1: "Active"}
active = st.sidebar.selectbox(
    'Physical Activity',
    options = list(active_dict.keys()),
    format_func=lambda x: active_dict.get(x)
)



# if st.button('Predict Cardio'):
#     input_data = pd.DataFrame([['age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo',
#        'cholesterol', 'gluc', 'smoke', 'alco', 'active']], columns = features)
    
#     # Data Scaling
#     input_scaler = scaler.transform(input_data)

#     # Model Prediction
#     prediction = model.predict(input_scaler)[0]

#     if prediction == 0:
#         st.write('Likely not to have cardiovascular disease')
#         st.success('No Cardiovascular Disease Found.')
#     else:
#         st.write('Likely to have cardiovascular disease')
#         st.error('Cardiovascular Disease Found.')




if st.button('Predict Cardio'):
    input_data = pd.DataFrame(
        [[age, gender, height, weight, ap_hi, ap_lo,
          cholestrol, gluc, smoke, alco, active]],
        columns=features
    )

    # Data Scaling
    input_scaler = scaler.transform(input_data)

    # Model Prediction
    prediction = model.predict(input_scaler)[0]

    if prediction == 0:
        st.write('Likely not to have cardiovascular disease')
        st.success('No Cardiovascular Disease Found.')
    else:
        st.write('Likely to have cardiovascular disease')
        st.error('Cardiovascular Disease Found.')

if st.button ('Predict Cardio'):
    payload = {
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "ap_hi": ap_hi,
        "ap_lo": ap_lo,
        "cholesterol": cholestrol,
        "gluc": gluc,
        "smoke": smoke,
        "alco": alco,
        "active": active
    }
    try:
        response = requests.post(f"{API_URL}", json=payload)
        
        if response.status_code == 200:
            result = response.json()
            
            if result['prediction Status'] == 0:
                st.write('Likely not to have cardiovascular disease')
                st.success('No Cardiovascular Disease Found.')
            else:
                st.write('Likely to have cardiovascular disease')
                st.error('Cardiovascular Disease Found.')
        else:
            st.error(f"API status code error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"API request error: {e}")
            
# Visualization
st.subheader('Visualization')

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='1.0f',xticklabels=['Predicted Healthy[0]', 'Predicted Unhealthy[1]'], 
            yticklabels=['Actual Healthy[0]', 'Actual Unhealthy[1]'], cmap='Blues', ax=ax)
st.pyplot(fig)