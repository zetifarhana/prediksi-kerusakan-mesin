import pickle
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt

model = pickle.load(open('model_prediksi_kerusakan_logreg_failtype.sav', 'rb'))

st.title('Prediksi Kerusakan Mesin')

#open file csv
df1 = pd.read_csv('predictive_maintenance.csv')

# Fungsi untuk halaman Deskripsi
def show_deskripsi():
    st.write("Selamat datang di aplikasi prediksi kerusakan mesin berbasis web.")
    st.write("<div style='text-align: justify;'>Aplikasi ini menggunakan teknologi <i>Machine Learning</i> untuk memberikan prediksi yang akurat terkait kemungkinan kerusakan mesin berdasarkan beberapa variabel kunci. Dengan memasukkan nilai-nilai seperti Type, Air Temperature, Process Temperature, Rotational Speed, Torque, dan Tool Wear, pengguna dapat dengan mudah mendapatkan perkiraan tingkat risiko kerusakan mesin. Model <i>Machine Learning</i> yang kuat di balik aplikasi ini telah dilatih menggunakan data historis yang luas yakni sejumlah kurang lebih 10.000 data, memungkinkan sistem memberikan prediksi yang handal. Aplikasi ini dirancang untuk membantu pengguna mengidentifikasi potensi masalah sebelum terjadinya kerusakan serius, memungkinkan perencanaan pemeliharaan yang lebih efisien dan pengoperasian mesin yang lebih handal. Sederhana, responsif, dan mudah digunakan, aplikasi ini menjadi mitra ideal dalam mengoptimalkan kinerja dan umur pakai mesin industri.</div>", unsafe_allow_html=True)
    st.write("Sumber data: https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset")
    st.write("Dibuat oleh Tim Prodi D3 Teknologi Informasi PNM - 2023")

# Fungsi untuk halaman Dataset
def show_dataset():
    st.header("Dataset")
    st.dataframe(df1)
    st.markdown("""
( 1 ) **Type**
   - Terdiri dari kode L, M, H, untuk Low (50% dari seluruh produk), Medium (30%), dan High (20%).
   - Sebagai varian kualitas produk dan nomor seri khusus varian.
  \n(
2 ) **Air Temperature (Suhu Udara)**
   - Suhu udara adalah suhu sekitar mesin atau peralatan.
   - Suhu udara yang ekstrem dapat memengaruhi suhu mesin dan kinerja komponen.
  \n(
3 ) **Process Temperature (Suhu Proses)**
   - Merupakan suhu yang diukur dalam proses produksi atau operasional mesin.
   - Suhu proses di luar rentang yang diinginkan dapat mempengaruhi kualitas produk dan merusak komponen mesin.
  \n(
4 ) **Rotational Speed (Kecepatan Putaran)**
   - Kecepatan putaran adalah kecepatan dimana mesin atau bagian mesin berputar.
   - Kecepatan putaran yang ekstrem dapat menyebabkan keausan, getaran, atau kegagalan komponen.
  \n(
5 ) **Torque (Torsi)**
   - Torsi adalah gaya yang dapat memutar objek sekitar sumbu putar.
   - Torsi berlebihan atau tidak memadai dapat mempengaruhi kinerja mesin dan menyebabkan kerusakan.
  \n(
6 ) **Tool Wear (Keausan Alat)**
   - Keausan alat merujuk pada penggunaan berlebihan atau penurunan kualitas alat pemotong atau alat lainnya.
   - Keausan alat yang berlebihan dapat mempengaruhi hasil produksi, memerlukan pemeliharaan lebih sering, dan dapat merusak bagian-bagian mesin.
""")

# Fungsi untuk halaman Grafik
def show_grafik():
    st.header("Grafik")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Air Temperature", "Process Temperature", "Rotational Speed", "Torque", "Tool Wear"])

    with tab1:
        st.write("Grafik Air Temperature")
        chart_airtemperature = pd.DataFrame(df1, columns=["Air temperature"])
        st.line_chart(chart_airtemperature)
    with tab2:
        st.write("Grafik Process Temperature")
        chart_processtemperature = pd.DataFrame(df1, columns=["Process temperature"])
        st.line_chart(chart_processtemperature)
    with tab3:
        st.write("Grafik Rotational Speed")
        chart_rotationalspeed = pd.DataFrame(df1, columns=["Rotational speed"])
        st.line_chart(chart_rotationalspeed)
    with tab4:
        st.write("Grafik Torque")
        chart_torque = pd.DataFrame(df1, columns=["Torque"])
        st.line_chart(chart_torque)
    with tab5:
        st.write("Grafik Toolwear")
        chart_toolwear = pd.DataFrame(df1, columns=["Tool wear"])
        st.line_chart(chart_toolwear)

def show_prediksi():
    st.header("Prediksi")
    st.write("Tentukan nilai-nilai pada variabel berikut untuk menentukan jenis kerusakan yang dialami oleh mesin:")
    type = st.slider('Type', 1, 3, 2)
    airtemperature = st.slider('Air temperature:', 295.3, 304.5, 300.0)
    processtemperature = st.slider('Process temperature:', 305.7, 313.8, 310.1)
    rotationalspeed = st.slider('Rotational speed:', 1168, 2886, 1503)
    torque = st.slider('Torque:', 3.8, 76.6, 40.1)
    toolwear = st.slider('Tool wear:', 0, 253, 108)

    if st.button('Prediksi'):
        car_prediction = model.predict([[type, airtemperature, processtemperature, rotationalspeed, torque, toolwear]])
        if car_prediction == 1:
            hasil = "No Failure"
        elif car_prediction == 2:
            hasil = "Heat Dissipation Failure"
        elif car_prediction == 3:
            hasil = "Power Failure"
        elif car_prediction == 4:
            hasil = "Overstrain Failure"
        elif car_prediction == 5:
            hasil = "Tool Wear Failure"
        st.write('Hasil prediksi :', hasil)

add_selectbox = st.sidebar.selectbox(
    "PILIH MENU",
    ("Deskripsi", "Dataset", "Grafik", "Prediksi")
)

if add_selectbox == "Deskripsi":
    show_deskripsi()
elif add_selectbox == "Dataset":
    show_dataset()
elif add_selectbox == "Grafik":
    show_grafik()
elif add_selectbox == "Prediksi":
    show_prediksi()
