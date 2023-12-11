import pickle
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt

model = pickle.load(open('model_prediksi_kerusakan_logreg.sav', 'rb'))

st.title('Prediksi Kerusakan Mesin')

st.header("Dataset")
#open file csv
df1 = pd.read_csv('predictive_maintenance.csv')
st.dataframe(df1)

type = st.number_input('Type:', min_value=0)
airtemperature = st.number_input('Air temperature:', min_value=0)
processtemperature = st.number_input('Process temperature:', min_value=0)
rotationalspeed = st.number_input('Rotational speed:', min_value=0)
torque = st.number_input('Torque:', min_value=0)
toolwear = st.number_input('Tool wear:', min_value=0)

if st.button('Prediksi'):
    car_prediction = model.predict([[type, airtemperature, processtemperature, rotationalspeed, torque, toolwear]])
    
    # convert float to string
    #hasil_str = np.array(car_prediction)
    #hasil_float = float(hasil_str[0][0])
    #hasil_formatted = f'Hasil Prediksi Kerusakan: {hasil_float:,.2f}'

    if car_prediction == 0:
        hasil = 'Tidak ada kerusakan mesin'
    else:
        hasil = 'Ada kerusakan mesin'

    st.write('Hasil prediksi :', hasil)
