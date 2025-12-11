📚 Sistem Kunjungan TBM

Aplikasi sederhana berbasis Python untuk mencatat data kunjungan di Taman Bacaan Masyarakat (TBM).
Proyek ini dibuat untuk memenuhi tugas UAS – mencakup penggunaan modul, package, OOP, percabangan, perulangan, serta koneksi database MySQL.

## Tampilan Aplikasi

### 1. Tampilan Dashboard
![Dashboard](assets/Screenshot%202025-12-11%20220225.png)

### 2. Tampilan Form Input
![Form Input](assets/Screenshot%202025-12-11%20222043.png)

### 3. Tampilan Data Kunjungan
![Data Kunjungan](assets/Screenshot%202025-12-11%20222057.png)



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
