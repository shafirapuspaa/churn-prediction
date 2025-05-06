import pandas as pd
import numpy as np

# import model final
from xgboost import XGBClassifier

# load model
import pickle
import joblib

import streamlit as st

#=====

# Judul utama
st.write("""
         <div style="text-align: center;">
         <h2>Churn Customer Prediction </h2>
         </div>
         """, unsafe_allow_html=True)

# sidebar menu for input
st.sidebar.header('Please Input Your Customer Feature')

# untuk input numerik
def user_iput():
    cred_score = st.sidebar.slider(label = 'Credit Score',min_value=350,max_value=850,value=500)
    balance = st.sidebar.slider(label = 'Balance',min_value=0,max_value=251000,value=10000)
    Salary = st.sidebar.slider(label = 'EstimatedSalary',min_value=11,max_value=200000,value=10000)

    age = st.sidebar.number_input(label='Age',max_value=92,min_value=18,value = 40)
    tenure = st.sidebar.number_input(label='Tenure',max_value=10,min_value=0)

    product = st.sidebar.number_input(label='NumOfProduct', max_value=5,min_value=1)
    hascard = st.sidebar.selectbox(label='HasCrCard',options=[0,1])
    member = st.sidebar.selectbox(label='IsActiveMember',options=[0,1])


    gender = st.sidebar.selectbox(label='Gender',options=['Female','Male'])
    geography = st.sidebar.selectbox(label='Geography',options=['France','Germany','Spain'])

    df = pd.DataFrame()
    df['CreditScore'] = [cred_score]
    df['Geography'] = [geography]
    df['Gender'] = [gender]
    df['Age'] =[age]
    df['Tenure'] =[tenure]
    df['Balance'] = [balance]
    df['NumOfProducts'] = [product]
    df['HasCrCard'] = [hascard]
    df['IsActiveMember'] = [member]
    df['EstimatedSalary'] = [Salary]
    return df

df_feature= user_iput()

#memanggil model
model = joblib.load('model_xgboost_joblib')

# predict
pred = model.predict(df_feature)


st.write('Tujuan dari project ini adalah menentukan apakah seorang customer akan melakukan churn (tidak menggunakan jasa lagi) dari bank ini.')

col1,col2 = st.columns(2)

with col1:
    st.subheader('Customer Characteristics')
    st.write(df_feature.transpose())

with col2:
    st.subheader('Predicted Result')
    if pred == [1]:
        st.write("<h3 style = 'color : red;'>Your Customer is likely to CHURN</h3>", unsafe_allow_html=True)
    else:
        st.write("<h3 style = 'color : green;'>Your Customer is predicted to STAY</h3>", unsafe_allow_html=True)