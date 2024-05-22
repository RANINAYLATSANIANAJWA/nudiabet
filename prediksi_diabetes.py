import streamlit as st
test =st.sidebar.selectbox("Prediksi Diabetes",["Diabetes","Prediksi Diabetes","Kelompok 7"])

import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

#halaman Diabetes

st.title("Pengertian Diabetes")
st.write("Diabetes melitus atau yang dikenal dengan kencing manis merupakan penyakit dimana kadar gula dalam darah cukup tinggi karena tubuh tidak dapat menggunakan insulin sehingga gula didalam darah tidak dapat dimetabolisme.")
st.image("Alat tes diabetes.jpeg.jpg")

st.title("Gejala Diabetes")
st.write("A. Sering kencing")
st.write("B. Rasa haus berlebihan")
st.write("C. Rasa lapar berlebihan")
st.write("D. Mudah lelah")
st.write("E. Kadar gula darah tinggi")
st.write("F. Luka lambat sembuh")

st.title("Faktor Penyebab Diabetes")
st.write("Faktor genetik")
st.write("Obesitas dan berat badan berlebih")
st.write("Usia")
st.write("Hipertens")
st.write("Gangguan Toleransi Glukosa")

st.title("Cara Mengontrol Diabetes")
st.image("Kontrol Diabetes.jpeg.jpg")
st.write("Diet Sehat dan Seimbang")
st.write("Olahraga Rutin")
st.write("Pemantauan Gula Darah")
st.write("Penggunaan Obat Secara Teratur")
st.write("Pemeriksaan Kesehatan Rutin")

# Load the trained model and scaler
def load_model():
    return pickle.load(open("diabetes_model.sav", "rb"))

def load_scaler():
    return pickle.load(open("scaler.sav", "rb"))

def predict_diabetes(input_data, model, scaler):
    # Preprocess input data
    std_data = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(std_data)

    return prediction

#halaman Prediksi Diabetes
if test == "Prediksi Diabetes":...

def main ():
 st.title('Prediksi Diabetes')
st.write('Masukkan data pasien untuk melakukan prediksi')

    # Define input fields for user to input patient data
pregnancies = st.number_input("Jumlah Kehamilan", min_value=0, max_value=17, step=1)
glucose = st.number_input("Glukosa (mg/dL)", min_value=0, max_value=200, step=1)
blood_pressure = st.number_input("Tekanan Darah (mm Hg)", min_value=0, max_value=122, step=1)
skin_thickness = st.number_input("Ketebalan Kulit (mm)", min_value=0, max_value=99, step=1)
insulin = st.number_input("Insulin (mu U/ml)", min_value=0, max_value=846, step=1)
bmi = st.number_input("Indeks Massa Tubuh (BMI)", min_value=0.0, max_value=67.1, step=0.1)
diabetes_pedigree = st.number_input("Riwayat Diabetes Keluarga", min_value=0.078, max_value=2.42, step=0.001)
age = st.number_input("Usia (tahun)", min_value=0, max_value=200, step=1)

    # Create a numpy array from the user input data
input_data = np.array([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]).reshape(1, -1)

    # Load the model and scaler
model = load_model()
scaler = load_scaler()

if st.button('Jalankan Prediksi'):
        # Perform prediction
        prediction = predict_diabetes(input_data, model, scaler)

        # Display prediction result
        if prediction[0] == 0:
            st.write("Pasien tidak terkena diabetes :D")
        else:
            st.write("Pasien terkena diabetes T_T")

if __name__ == '__main__':
    main ()

#halaman kelompok 7
if test == "Kelompok 7":
    st.title("Website ini dirancang untuk mempermudah tenaga medis untuk memprediksi penyakit diabetes pada pasien")

st.header("Website ini dirancang oleh")
st.write("1. Fitri Syahrani Prasetyaningrum (2360129)")
st.write("2. Muhammad Ariel. Z (2360181)")
st.write("3. Najwa Nubzatussofwa(2360201)")
st.write("4. Nayla Khairunnisa (2360208)")
st.write("5. Tsania Zahra (2360280)")
st.image("our members.jpg")