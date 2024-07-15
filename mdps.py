# -*- coding: utf-8 -*-
"""
 Created on oct 3rd 11:53:51 2023

 @author: reddy uday
"""

import pickle
import streamlit as st
import pandas as pd
import emoji

# Load models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
Breast_cancer_model = pickle.load(open('Breast_cancer_model.sav', 'rb'))

# Set up page configuration
st.set_page_config(
    page_title="medXpert💉",
    page_icon="💉",
    layout="wide"
)

# Sidebar for navigation
with st.sidebar:
    selected = st.selectbox(
        'PREDICTION MENU:',
        ['Diabetes Prediction 🩸', 'Heart Disease Prediction ❤️',"Breast Cancer Prediction 😷", "Parkinson's Prediction 🧠"]
    )

# Heading for Multiple Disease Prediction System
st.title("MULTIPLE DISEASE PREDICTIVE-medXpert 💉")

# Emojis for each prediction category
st.write(
    f"🩸 *Diabetes Prediction*  {'  ' if selected == 'Diabetes Prediction 🩸' else ''}",
    f"❤️ *Heart Disease Prediction*  {'  ' if selected == 'Heart Disease Prediction ❤️' else ''}",
    f"😷 *Breast Cancer Prediction*  {'  ' if selected == 'Breast Cancer Prediction 😷' else ''}",
    f"🧠 *Parkinson's Prediction*  {'  ' if selected == 'Parkinsons Prediction 🧠' else ''}"
)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction 🩸':
    st.title('🩸 Diabetes Prediction using ML 🩸')

    # Getting input data from the user
    features = ['Pregnancies', 'Glucose', 'Blood Pressure', 'Skin Thickness', 'Insulin', 'BMI',
                'Diabetes Pedigree Function', 'Age']

    user_input = [st.text_input(f'{feature}:') for feature in features]
    user_input = [float(value) if value.strip() != '' else 0.0 for value in user_input]

    # Code for Prediction
    if st.button('Diabetes Test Result 🤞🏼'):
        diab_prediction = diabetes_model.predict([user_input])
        result = 'The person is diabetic 😢' if diab_prediction[0] == 1 else 'The person is not diabetic 🤩'
        st.success(result)

# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction ❤️':
    st.write('<div id="heart_disease_prediction"></div>', unsafe_allow_html=True)
    st.title('❤️ Heart Disease Prediction using ML ❤️')

    # Getting input data from the user
    features = ['Age', 'Sex', 'Chest Pain Types', 'Resting Blood Pressure', 'Serum Cholestoral',
                'Fasting Blood Sugar', 'Resting Electrocardiographic Results', 'Max Heart Rate',
                'Exercise Induced Angina', 'ST Depression', 'Slope of Peak Exercise ST Segment',
                'Major Vessels Colored', 'Thal']

    user_input = [st.text_input(f'{feature}:') for feature in features]
    user_input = [float(value) if value.strip() != '' else 0.0 for value in user_input]

    # Code for Prediction
    if st.button('Heart Disease Test Result 🤞🏼'):
        heart_prediction = heart_disease_model.predict([user_input])
        result = 'The person has heart disease 😢' if heart_prediction[
                                                       0] == 1 else 'The person does not have heart disease 🤩'
        st.success(result)

# Breast Cancer Prediction Page
elif selected == "Breast Cancer Prediction 😷":
    st.title("😷 Breast Cancer Prediction Prediction using ML 😷")

    # Getting input data from the user
    features = ['Mean Radius','Mean Texture','Mean Perimeter','Mean Area','Mean Smoothness']

    user_input = [st.text_input(f'{feature}:') for feature in features]
    user_input = [float(value) if value.strip() != '' else 0.0 for value in user_input]

    # Code for Prediction
    if st.button("Check Test Result 🤞🏼"):
        Breast_cancer_prediction = Breast_cancer_model.predict([user_input])
        result = "The person has Breast Cancer 😢" if Breast_cancer_prediction[
                                                             0] == 1 else "The person does not have Breast Cancer 🤩"
        st.success(result)

# Parkinson's Prediction Page
elif selected == "Parkinson's Prediction 🧠":
    st.title("🧠 Parkinson's Disease Prediction using ML 🧠")

    # Getting input data from the user
    features = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
                'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
                'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR',
                'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE']

    user_input = [st.text_input(f'{feature}:') for feature in features]
    user_input = [float(value) if value.strip() != '' else 0.0 for value in user_input]

    # Code for Prediction
    if st.button("Parkinson's Test Result 🤞🏼"):
        parkinsons_prediction = parkinsons_model.predict([user_input])
        result = "The person has Parkinson's disease 😢" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease 🤩"
        st.success(result)
