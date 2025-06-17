# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Jaya Jaya Institut menghadapi sejumlah tantangan serius terkait ketidakselesaian studi oleh sebagian mahasiswa. Berdasarkan data internal, tingkat dropout mahasiswa melebihi 30% dalam beberapa tahun terakhir. Hal ini berdampak pada reputasi institusi, efektivitas penggunaan sumber daya, dan pencapaian target akademik.

Beberapa permasalahan utama yang dihadapi antara lain:

1. **Tingginya tingkat dropout mahasiswa**, yang berdampak pada citra dan kualitas institusi secara keseluruhan.
2. **Ketidakjelasan faktor dominan yang menyebabkan mahasiswa mengalami dropout**, sehingga menyulitkan pengambilan keputusan berbasis data.
3. **Distribusi dropout yang tidak merata antar jurusan dan kebangsaan**, menunjukkan perlunya kebijakan yang lebih terarah.
4. **Ketiadaan sistem prediktif untuk mengidentifikasi mahasiswa berisiko dropout sejak dini.**
5. **Kurangnya wawasan terkait keterkaitan antara performa akademik dan potensi dropout**, seperti nilai rata-rata semester atau jumlah evaluasi yang diterima.

Permasalahan-permasalahan ini menjadi dasar dilakukannya analisis prediktif untuk membantu institusi dalam memahami dan menanggulangi risiko dropout secara lebih efektif.

### Cakupan Proyek
1. Pemahaman Data (Data Understanding), proyek ini dimulai dengan eksplorasi data mahasiswa yang mencakup aspek demografis, akademik, dan administratif. Langkah ini bertujuan untuk memahami pola dalam data serta mengidentifikasi variabel-variabel utama yang berpengaruh terhadap status kelulusan mahasiswa.
2. Pra-pemrosesan Data (Data Preprocessing), sebelum membangun model prediksi, dilakukan pra-pemrosesan data untuk memastikan kualitasnya dan penyesuaian outlier, serta encoding variabel kategorikal agar dapat digunakan dalam analisis. Selain itu, dilakukan feature engineering untuk meningkatkan akurasi model dengan mengekstrak informasi yang lebih relevan dari data yang tersedia.
3. Pemodelan (Modeling), menggunakan model klasifikasi seperti Random Forest untuk memprediksi status mahasiswa.
4. Evaluasi Model (Evaluation), setelah model dikembangkan dilakukan evaluasi menggunakan metrik seperti akurasi, precision, recall, dan F1-score. Evaluasi ini bertujuan untuk mengukur efektivitas model dalam memprediksi status mahasiswa serta memastikan bahwa model yang dipilih memiliki performa yang optimal dalam mendeteksi risiko dropout.
5. Implementasi dan Rekomendasi, model terbaik disimpan dalam format (.joblib) agar dapat digunakan lebih lanjut dalam sistem akademik.
6. Visualisasi Data dan Dashboard (Data Visualization & Dashboarding), untuk menyajikan hasil analisis secara lebih intuitif dikembangkan dashboard interaktif menggunakan Metabase. Dashboard ini memungkinkan eksplorasi data berdasarkan Status Mahasiswa dan Gender, serta menampilkan informasi utama seperti total mahasiswa berdasarkan status mahasiswa dan gender, distribusi kewarganegaraan, jurusan dengan dropout tertinggi, dan faktor utama yang berkontribusi terhadap dropout.
7. Interpretasi dan Insight Bisnis, hasil visualisasi dan model prediksi dianalisis lebih lanjut melalui dashboard interaktif di Streamlit, yang memungkinkan eksplorasi pola dropout berdasarkan faktor seperti status beasiswa, keterlambatan pembayaran, atau status pernikahan. Selain itu, dashboard membantu mengidentifikasi jurusan dan kewarganegaraan yang paling rentan terhadap dropout, sehingga dapat digunakan untuk evaluasi kurikulum dan kebijakan pendidikan. Dengan pendekatan ini, institusi dapat memahami tren dropout secara lebih dinamis dan mengambil langkah intervensi yang tepat berdasarkan data yang telah divisualisasikan.

### Persiapan
Sumber Data
Dataset yang digunakan dalam proyek ini berisi informasi akademik dan administratif mahasiswa yang mencakup data demografis (usia saat masuk, kebangsaan), data akademik (nilai masuk, rata-rata nilai semester, jumlah mata kuliah lulus), data evaluasi (jumlah evaluasi per semester), data finansial (status pembayaran, penerimaan beasiswa), dan label target berupa status mahasiswa (Dropout, Enrolled, Graduate).

Dataset ini terdiri dari 4.424 baris dan 37 kolom, dan digunakan untuk melatih model machine learning dalam memprediksi risiko mahasiswa mengalami dropout.

Dataset dapat diakses melalui tautan berikut: (https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)


Setup environment:

1. Proyek ini awalnya dikerjakan menggunakan Google Colab dan kemudian dilanjutkan secara lokal menggunakan Visual Studio Code tanpa menggunakan Conda. Untuk menjalankan proyek di lingkungan yang terisolasi, ikuti langkah-langkah berikut:

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Gunakan docker dan pastikan docker sudah terinstall.

```
docker compose up -d
```

3. Login Metabase:

```
username: root1@gmail.com
password: root12345
```

4. Deploy Streamlit App
```
streamlit run app.py
```


## Business Dashboard
Business Dashboard yang dibuat menggunakan Metabase berfungsi untuk analisis data mahasiswa, khususnya dalam memahami pola dropout berdasarkan berbagai faktor akademik dan finansial.  Berikut tampilannya:
![tiani_ayu-dashboard-1](https://github.com/user-attachments/assets/38126783-949f-4bce-ad87-22bffb9ceca9)

 ![tiani_ayu-dashboard-2](https://github.com/user-attachments/assets/0060e2d0-11cd-4b34-99d1-7cb11a9460c4)

## Menjalankan Sistem Machine Learning
Sistem Machine Learning yang dibuat berfungsi untuk memprediksi kemungkinan mahasiswa mengalami dropout berdasarkan data akademik dan finansial mereka. Dashboard ini memungkinkan pengguna untuk: 
- Memasukkan data akademik dan finansial mahasiswa
- Menjalankan model prediksi dropout secara real-time
- Mendapatkan hasil prediksi apakah mahasiswa akan dropout, tetap terdaftar, atau lulus

Menjalankan model di Streamlit (lokal):
```
streamlit run app.py
```
Link Akses Prototype Machine Learning: [Streamlit App](https://dudidudidam.streamlit.app/)
![image](https://github.com/user-attachments/assets/58a8ff17-e011-4767-8803-45c3712a9e59)

![image](https://github.com/user-attachments/assets/f3f3dd9e-40ba-4602-9ba5-a5e2f68fab09)

## Conclusion
Berdasarkan hasil pemodelan dan evaluasi menggunakan beberapa algoritma klasifikasi, model terbaik yang dipilih menunjukkan performa yang cukup baik dalam memprediksi status mahasiswa dengan akurasi sebesar 76.27%. Model ini mampu mengidentifikasi mahasiswa yang berpotensi mengalami dropout dengan cukup baik, terutama pada kategori Dropout dan Graduate, yang masing-masing memiliki f1-score sebesar 0.79 dan 0.84.

Secara keseluruhan, hasil classification report menunjukkan bahwa model memiliki:
- Precision tertinggi pada kategori Dropout (0.84), yang berarti model cukup akurat dalam mengidentifikasi mahasiswa yang dropout.
- Recall tertinggi pada kategori Graduate (0.94), menunjukkan bahwa model berhasil mengenali sebagian besar mahasiswa yang berhasil lulus.
- Rata-rata makro f1-score sebesar 0.68, dan rata-rata tertimbang (weighted average) f1-score sebesar 0.75.

Proyek ini berhasil mengidentifikasi faktor utama yang berkontribusi terhadap tingkat dropout mahasiswa. Hasil ini mengindikasikan bahwa model cukup andal digunakan sebagai alat bantu untuk melakukan deteksi dini terhadap potensi mahasiswa yang berisiko dropout. Rekomendasi utama dari proyek ini mencakup integrasi model prediksi ke dalam sistem monitoring mahasiswa, fokus intervensi pada mahasiswa dengan profil risiko tinggi, serta pengembangan lanjutan seperti pengujian real-time atau integrasi ke dalam sistem informasi akademik kampus. 

### Rekomendasi Action Items
Berdasarkan hasil analisis data dan pemodelan machine learning terhadap kasus mahasiswa dropout, berikut adalah beberapa rekomendasi action items yang dapat dilakukan oleh perusahaan edutech atau institusi pendidikan:
- action item 1. Implementasi Sistem Pendeteksi Dini Dropout (Early Warning System)
- action item 2. Fokus Intervensi pada Jurusan dan Kelompok Mahasiswa Rentan
- action item 3. Penguatan Program Beasiswa dan Pendampingan Keuangan
- action item 4. Monitoring dan Evaluasi Berkala Terhadap Data Mahasiswa
