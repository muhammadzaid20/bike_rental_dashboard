
# Bike Rental Analysis Dashboard 🚴‍♂️✨

## Overview
Dashboard ini bertujuan untuk menganalisis data penyewaan sepeda dengan berbagai visualisasi yang interaktif dan informatif. Data yang digunakan terdiri dari dua set: *hourly* dan *daily*, yang masing-masing memberikan wawasan tentang pola penggunaan sepeda berdasarkan waktu dan kondisi tertentu.

---

## Setup Environment

### **Menggunakan Anaconda**
1. **Buat Environment Baru**
   ```bash
   conda create --name Submission python=3.9
   ```
2. **Aktifkan Environment**
   ```bash
   conda activate Submission
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### **Menggunakan Pipenv**
1. **Inisialisasi Proyek**
   ```bash
   mkdir Submission
   cd Submission
   pipenv install
   ```
2. **Masuk ke Virtual Environment**
   ```bash
   pipenv shell
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## Run Dashboard
Setelah semua dependencies terinstall, jalankan aplikasi Streamlit dengan perintah:
```bash
streamlit run main.py
```

---

## Project Structure
Berikut adalah struktur folder dari proyek ini:

```
Submission
├───Dashboard
| └───data_loader.py
| └───main.py
| └───preprocessing.py
| └───utils.py
| └───visualization.py
├───Data
| ├───hour.csv
| └───day.csv
├───Submission_Analisis_Data.ipynb
├───README.md
└───requirements.txt
└───url.txt              
```

---

## Dataset
Pastikan file dataset berikut sudah tersedia di direktori:
- **Hourly Dataset**: `\Submission\Data\hour.csv`
- **Daily Dataset**: `\Submission\Data\day.csv`

---

## Troubleshooting
Jika terjadi masalah saat menjalankan dashboard:
1. Pastikan semua dependencies sudah terinstall dengan benar.
2. Pastikan file dataset berada pada path yang sesuai.
3. Gunakan perintah berikut untuk memeriksa versi library yang terinstall:
   ```bash
   pip list
   ```

---

## Contribute
Anda memiliki ide untuk meningkatkan dashboard ini? Silakan kirimkan *pull request* atau diskusikan ide Anda di bagian *Issues*.

---
