import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.joblib")

# Judul aplikasi
st.title("Prediksi Dropout Mahasiswa - Jaya Jaya Institut")
st.markdown("""
Masukkan data berikut untuk memprediksi status kelulusan mahasiswa.
""")

# Form input
with st.form("input_form"):
    # Fitur penting
    usia = st.number_input("Usia saat masuk", 15, 70, 18)
    admission_grade = st.slider("Nilai masuk", 95.0, 200.0, 120.0)
    previous_grade = st.slider("Nilai kualifikasi sebelumnya", 0.0, 200.0, 100.0)

    first_sem_grade = st.slider("Rata-rata nilai semester 1", 0.0, 20.0, 10.0)
    second_sem_grade = st.slider("Rata-rata nilai semester 2", 0.0, 20.0, 10.0)

    first_sem_approved = st.number_input("Jumlah mata kuliah lulus semester 1", 0, 20, 5)
    second_sem_approved = st.number_input("Jumlah mata kuliah lulus semester 2", 0, 20, 5)

    first_sem_evals = st.number_input("Jumlah evaluasi semester 1", 0, 100, 10)
    second_sem_evals = st.number_input("Jumlah evaluasi semester 2", 0, 100, 10)

    tuition_paid = st.radio("Apakah biaya kuliah dibayar tepat waktu?", ['Ya', 'Tidak'])

    scholarship = st.radio("Penerima beasiswa?", ['Ya', 'Tidak'])

    # Fitur kategorikal
    course = st.selectbox("Program Studi", [
        'Biofuel Production Technologies', 'Animation and Multimedia Design',
        'Social Service (evening attendance)', 'Agronomy', 'Communication Design',
        'Veterinary Nursing', 'Informatics Engineering', 'Equinculture', 'Management',
        'Social Service', 'Tourism', 'Nursing', 'Oral Hygiene',
        'Advertising and Marketing Management', 'Journalism and Communication',
        'Basic Education', 'Management (evening attendance)'
    ])

    nationality = st.selectbox("Kebangsaan", [
        'Portuguese', 'German', 'Spanish', 'Italian', 'Dutch', 'English', 'Lithuanian',
        'Angolan', 'Cape Verdean', 'Guinean', 'Mozambican', 'Santomean', 'Turkish',
        'Brazilian', 'Romanian', 'Moldova (Republic of)', 'Mexican', 'Ukrainian',
        'Russian', 'Cuban', 'Colombian'])

    submitted = st.form_submit_button("Prediksi")

if submitted:
    # Mapping
    course_map = {
        'Biofuel Production Technologies': 9254, 'Animation and Multimedia Design': 9070,
        'Social Service (evening attendance)': 9556, 'Agronomy': 9238, 'Communication Design': 9119,
        'Veterinary Nursing': 9130, 'Informatics Engineering': 9070, 'Equinculture': 9287,
        'Management': 9147, 'Social Service': 9781, 'Tourism': 9991, 'Nursing': 9500,
        'Oral Hygiene': 9238, 'Advertising and Marketing Management': 9257,
        'Journalism and Communication': 9357, 'Basic Education': 9014,
        'Management (evening attendance)': 9136
    }

    nationality_map = {
        'Portuguese': 1, 'German': 2, 'Spanish': 6, 'Italian': 10, 'Dutch': 11,
        'English': 13, 'Lithuanian': 14, 'Angolan': 6, 'Cape Verdean': 3,
        'Guinean': 4, 'Mozambican': 5, 'Santomean': 7, 'Turkish': 16,
        'Brazilian': 8, 'Romanian': 9, 'Moldova (Republic of)': 12,
        'Mexican': 17, 'Ukrainian': 18, 'Russian': 19, 'Cuban': 20, 'Colombian': 21
    }

    # Bangun data input
    data = {
        'Age_at_enrollment': usia,
        'Admission_grade': admission_grade,
        'Previous_qualification_grade': previous_grade,
        'Curricular_units_1st_sem_grade': first_sem_grade,
        'Curricular_units_2nd_sem_grade': second_sem_grade,
        'Curricular_units_1st_sem_approved': first_sem_approved,
        'Curricular_units_2nd_sem_approved': second_sem_approved,
        'Curricular_units_1st_sem_evaluations': first_sem_evals,
        'Curricular_units_2nd_sem_evaluations': second_sem_evals,
        'Tuition_fees_up_to_date_No': 0 if tuition_paid == 'Ya' else 1,
        'Scholarship_holder': 1 if scholarship == 'Ya' else 0,
        'Course': course_map.get(course, 0),
        'Nacionality': nationality_map.get(nationality, 0)
    }

    df_input = pd.DataFrame([data])

    # Pastikan semua kolom sesuai dengan model
    for col in model.feature_names_in_:
        if col not in df_input.columns:
            df_input[col] = 0
    df_input = df_input[model.feature_names_in_]

    # Prediksi
    prediction = model.predict(df_input)[0]
    label_map = {0: 'Dropout', 1: 'Enrolled', 2: 'Graduate'}

    # Tampilkan hasil
    st.subheader("Hasil Prediksi")
    st.write(f"Status mahasiswa yang diprediksi: **{label_map[prediction]}** 🎓")
