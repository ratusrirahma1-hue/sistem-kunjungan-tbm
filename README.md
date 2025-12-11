📚 Sistem Kunjungan TBM

Aplikasi sederhana berbasis Python untuk mencatat data kunjungan di Taman Bacaan Masyarakat (TBM).
Proyek ini dibuat untuk memenuhi tugas UAS – mencakup penggunaan modul, package, OOP, percabangan, perulangan, serta koneksi database MySQL.

## 📸 Preview Aplikasi Kunjungan TBM

### 🖼️ Tampilan 1
<img src="assets/ss_222057.png" width="450">

### 🖼️ Tampilan 2
<img src="assets/ss_220225.png" width="450">

### 🖼️ Tampilan 3
<img src="assets/ss_222043.png" width="450">


✨ Fitur Utama

Melihat data kunjungan TBM

Menambah data kunjungan

Menghapus data kunjungan

Melihat daftar kategori kegiatan

Struktur program dipisah per file (modular & rapi)

🗂️ Struktur Folder
UAS-PYTHON/
│── app.py
│── main.py
│── models.py
│── database.py
│── assets/
│     └── (file foto, icon, dokumen jika ada)
└── sql/
      └── tbm_database.sql

🛢 Struktur Database (MySQL)

Database: tbm_kunjungan

Tabel: kategori
id	nama
1	Membaca Buku
2	Belajar / Les
3	Pinjam Buku
4	Mengembalikan Buku
5	Diskusi / Kelas Literasi
6	Kolaborasi
Tabel: kunjungan

| id | nama_pengunjung | kategori_id | tanggal |

🚀 Cara Menjalankan

Import file SQL ke MySQL (Laragon/XAMPP)

Install package:

pip install mysql-connector-python


Jalankan aplikasi:

py main.py

🧰 Teknologi yang Digunakan

Python 3

MySQL

OOP (Class & Object)

Modular Programming (per file)

CRUD dasar

🧑‍💻 Tujuan Pengerjaan

Proyek ini dibuat untuk:

Mengimplementasikan materi Python (modul, package, perulangan, percabangan, OOP)

Membuat aplikasi console sederhana

Melatih pembuatan sistem pencatatan terstruktur

📄 Lisensi

Proyek ini bebas digunakan untuk pembelajaran.
