# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Jaya Jaya Institut menghadapi permasalahan signifikan terkait tingginya angka mahasiswa yang tidak menyelesaikan studinya (dropout). Fenomena ini dapat berdampak negatif terhadap reputasi institusi, efisiensi operasional, dan pencapaian target akademik. Permasalahan spesifik yang ingin diselesaikan antara lain:
1. Faktor apa saja yang paling dominan pada mahasiswa dropout?
2. Berapa banyak mahasiswa yang dropout dan graduate secara keseluruhan?
3. Jurusan mana yang paling terdampak oleh tingkat dropout?
4. Negara atau kebangsaan mana yang memiliki tingkat dropout tertinggi?
5. Bagaimana distribusi nilai rata-rata mahasiswa yang dropout dibandingkan dengan yang graduate?

### Cakupan Proyek
1. Pemahaman Data (Data Understanding):
  - Mengeksplorasi data mahasiswa, termasuk informasi demografis, akademik, dan administratif.
  - Mengidentifikasi variabel-variabel penting yang berkaitan dengan status kelulusan mahasiswa.
2. Pra-pemrosesan Data (Data Preprocessing):
  - Menangani data kosong, outlier, dan melakukan encoding pada variabel kategorikal.
  - Melakukan feature engineering untuk meningkatkan performa model prediksi.
3. Pemodelan (Modeling):
  - Membangun beberapa model klasifikasi seperti Random Forest, XGBoost, SVM, dan Decision Tree.
  - Melatih dan menguji performa model menggunakan data historis.
4. Evaluasi Model (Evaluation):
  - Mengevaluasi performa model berdasarkan metrik seperti akurasi, precision, recall, dan f1-score.
  - Memilih model terbaik yang dapat digunakan untuk mendeteksi potensi dropout.
5. Implementasi dan Rekomendasi:
  - Menyimpan model dalam format .joblib untuk dapat digunakan lebih lanjut.
  - Memberikan rekomendasi penggunaan model bagi pihak institusi untuk proses bimbingan dan intervensi dini.
6. Visualisasi Data dan Dashboard (Data Visualization & Dashboarding):
  - Mengembangkan dashboard interaktif menggunakan Metabase untuk menyajikan hasil analisis dalam bentuk visual yang mudah dipahami.
  - Menyediakan fitur filter berdasarkan Status (Dropout, Graduate, Enrolled) dan Gender (Male, Female) agar pengguna dapat melakukan eksplorasi data secara dinamis.
  - Menampilkan headline utama seperti total mahasiswa dropout, jurusan dengan dropout tertinggi, serta faktor-faktor yang paling berkontribusi terhadap kegagalan mahasiswa.
  - Visualisasi mencakup:
   - Total mahasiswa berdasarkan status dan gender
   - Distribusi kewarganegaraan mahasiswa
   - Jurusan dengan dropout tertinggi
   - Faktor penyebab dropout berdasarkan delapan kategori dominan
7. Interpretasi dan Insight Bisnis (Insight Generation):
Menginterpretasi hasil visualisasi dan model prediksi untuk menemukan pola dropout mahasiswa berdasarkan karakteristik tertentu seperti status beasiswa, keterlambatan pembayaran, atau status pernikahan.
  - Mengidentifikasi jurusan dan kewarganegaraan yang paling rentan terhadap dropout untuk keperluan evaluasi kurikulum dan kebijakan pendidikan.
  - Menghubungkan performa akademik mahasiswa dengan faktor ekonomi makro seperti tingkat pengangguran dan inflasi sebagai pendekatan tambahan untuk analisis prediktif yang lebih luas.
8. Kesimpulan dan Tindak Lanjut (Conclusion & Next Steps):
  - Proyek berhasil mengidentifikasi faktor-faktor utama yang berkontribusi terhadap tingkat dropout mahasiswa.
  - Model terbaik dari proses evaluasi dapat digunakan untuk memprediksi risiko dropout dan mendukung intervensi proaktif oleh pihak kampus.
  - Rekomendasi utama:
   - Gunakan model prediksi sebagai bagian dari sistem monitoring mahasiswa
   - Fokuskan program intervensi pada mahasiswa dengan profil risiko tinggi berdasarkan fitur yang paling memengaruhi
  - Pertimbangkan pengembangan lanjutan seperti pengujian real-time atau integrasi ke dalam sistem informasi akademik kampus

### Persiapan

Sumber Dataset yang digunakan dalam proyek ini berisi informasi akademik dan administratif mahasiswa, termasuk:
- Data demografis = Usia saat masuk, kebangsaan.
- Data akademik = Nilai masuk, nilai kualifikasi sebelumnya, rata-rata nilai semester, jumlah mata kuliah yang lulus.
- Data evaluasi = Jumlah evaluasi akademik per semester.
- Data finansial = Status pembayaran biaya kuliah dan penerimaan beasiswa.
- Label target = Status mahasiswa (Dropout, Enrolled, Graduate).

[Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)
memiliki 4.424 baris dengan 37 kolom digunakan untuk melatih model Machine Learning dalam memprediksi kemungkinan mahasiswa mengalami dropout, tetap terdaftar, atau lulus.

Setup environment:
Agar proyek ini dapat dijalankan dengan lingkungan yang terisolasi dan stabil, ikuti langkah-langkah berikut:

1. Gunakan Google Colab atau Jupyter Notebook untuk menjalankan keseluruhan isi file `notebook.ipynb` guna meninjau hasil analisis data, temuan, serta wawasan yang diperoleh.

2. Menginstal Dependensi dari requirements.txt. Pastikan semua pustaka yang diperlukan telah terinstal sebelum menjalankan proyek.

```
pip install pipreqs
pipreqs . --force
```

3. Gunakan docker dan pastikan docker sudah terinstall.

```
docker-compose up -d
```

4. Login Metabase:

```
username: root1@mail.com
password: root123
```

5. Deploy Streamlit App
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
Berdasarkan hasil pemodelan dan evaluasi menggunakan beberapa algoritma klasifikasi, model terbaik yang dipilih menunjukkan performa yang cukup baik dalam memprediksi status mahasiswa (Dropout, Enrolled, Graduate) dengan akurasi sebesar 76.27%. Model ini mampu mengidentifikasi mahasiswa yang berpotensi mengalami dropout dengan cukup baik, terutama pada kategori Dropout dan Graduate, yang masing-masing memiliki f1-score sebesar 0.79 dan 0.84.

Secara keseluruhan, hasil classification report menunjukkan bahwa model memiliki:
- Precision tertinggi pada kategori Dropout (0.84), yang berarti model cukup akurat dalam mengidentifikasi mahasiswa yang dropout.
- Recall tertinggi pada kategori Graduate (0.94), menunjukkan bahwa model berhasil mengenali sebagian besar mahasiswa yang berhasil lulus.
- Rata-rata makro f1-score sebesar 0.68, dan rata-rata tertimbang (weighted average) f1-score sebesar 0.75.

Hasil ini mengindikasikan bahwa model cukup andal digunakan sebagai alat bantu untuk melakukan deteksi dini terhadap potensi mahasiswa yang berisiko dropout, yang selanjutnya dapat ditindaklanjuti dengan intervensi atau bimbingan khusus dari pihak institusi.

Untuk meningkatkan performa model ke depan, disarankan untuk:
- Melakukan balancing data untuk kategori Enrolled.
- Mengeksplorasi tambahan fitur yang lebih representatif.
- Mengintegrasikan faktor-faktor eksternal seperti kondisi ekonomi dan psikologis mahasiswa.
- Melakukan uji coba penggunaan model dalam skenario nyata secara bertahap.

Dengan demikian, proyek ini memberikan solusi data-driven yang dapat digunakan pihak kampus dalam upaya pengurangan angka dropout dan peningkatan kualitas layanan pendidikan secara berkelanjutan.

### Rekomendasi Action Items
Berdasarkan hasil analisis data dan pemodelan machine learning terhadap kasus mahasiswa dropout, berikut adalah beberapa rekomendasi action items yang dapat dilakukan oleh perusahaan edutech atau institusi pendidikan:
- action item 1. Implementasi Sistem Pendeteksi Dini Dropout (Early Warning System)
- action item 2. Fokus Intervensi pada Jurusan dan Kelompok Mahasiswa Rentan
- action item 3. Penguatan Program Beasiswa dan Pendampingan Keuangan
- action item 4. Monitoring dan Evaluasi Berkala Terhadap Data Mahasiswa
