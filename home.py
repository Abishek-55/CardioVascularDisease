import os
import numpy as np
import pandas as pd
import streamlit as st


def home():
    st.Page('home.py', title = 'Home')
    st.header('Welcome to the Cardiovascular Disease Prediction App')


pages = {
    "Home": {
        st.Page(home)
    },
    "Models": {
        st.Page('app/logistic.py', title = 'Logistic'),
        st.Page('app/svm.py', title = 'SVM')
    }
}


pg = st.navigation(pages, position = 'top')
pg.run()
# st.set_page_config(page_title="Cardiovascular Disease Prediction", page_icon="❤️")

# st.header("Cardiovascular Disease Prediction")
st.subheader("Using Logistic Regression")




st.sidebar.write("Cardio Features")

# age = st.sidebar.slider(
#     'Age',
#     max_value = 70,
#     min_value = 21,
#     value = 60,
#     step = 1
# )

# gender_dict = {1: "Female", 2: "Male"}
# # gender = st.sidebar.radio(
# #     'Gender',
# #     # get key
# #     options=list(gender_dict.keys()),
# #     # get values
# #     format_func=lambda x: gender_dict.get(x)
# # )


# gender = st.sidebar.selectbox(
#     'Gender',
#     options = list(gender_dict.keys()),
#     format_func=lambda x: gender_dict.get(x)
# )

# height = st.sidebar.slider(
#     'Height',
#     max_value = 200,
#     min_value = 136,
#     value = 145,
#     step = 1
# )

# weight = st.sidebar.slider(
#     'Weight',
#     max_value = 120,
#     min_value = 35,
#     value = 60,
#     step = 1
# )


# ap_hi = st.sidebar.slider(
#     'Systolic Pressure',
#     max_value = 200,
#     min_value = 90,
#     value = 120,
#     step = 1
# )
# ap_lo = st.sidebar.slider(
#     'Disystolic Pressure',
#     max_value = 100,
#     min_value = 50,
#     value = 80,
#     step = 1
# )
# cholesterol_dict = {1: "Low Cholesterol",2: "Mild Cholesterol", 3: "High Cholesterol"}
# cholestrol = st.sidebar.selectbox(
#     'Cholesterol',
#     options = list(cholesterol_dict.keys()),
#     format_func=lambda x: cholesterol_dict.get(x)
# )

# gluc_dict = {1: "Low Glucose",2: "Mild Glucose", 3: "High Glucose"}

# gluc = st.sidebar.selectbox(
#     'Glucose',
#     options = list(gluc_dict.keys()),
#     format_func=lambda x: gluc_dict.get(x)
# )

# smoke_dict = {0: "Non-Smoker", 1: "Smoker"}
# smoke = st.sidebar.selectbox(
#     'Smoker',
#     options = list(smoke_dict.keys()),
#     format_func=lambda x: smoke_dict.get(x)
# )

# alco_dict = {0: "Non-Alcoholic", 1: "Alcoholic"}
# alco = st.sidebar.selectbox(
#     'Alcoholic',
#     options = list(alco_dict.keys()),
#     format_func=lambda x: alco_dict.get(x)
# )

# active_dict = {0: "Inactive", 1: "Active"}
# active = st.sidebar.selectbox(
#     'Physical Activity',
#     options = list(active_dict.keys()),
#     format_func=lambda x: active_dict.get(x)
# )