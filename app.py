from database import Database
from models import Kunjungan

class TBMApp:
    def __init__(self):
        self.db = Database()

    def list_kunjungan(self):
        data = self.db.query("""
            SELECT kunjungan.*, kategori.nama AS kategori_nama
            FROM kunjungan
            LEFT JOIN kategori ON kategori.id = kunjungan.kategori_id
        """).fetchall()

        if not data:
            print("\nBelum ada data kunjungan.")
            return
        
        print("\n=== DAFTAR KUNJUNGAN TBM ===")
        for k in data:
            print(f"[{k['id']}] {k['nama_pengunjung']} | {k['kategori_nama']} | {k['tanggal']}")

    def list_kategori(self):
        data = self.db.query("SELECT * FROM kategori").fetchall()
        print("\n=== KATEGORI KUNJUNGAN TBM ===")
        for k in data:
            print(f"{k['id']}. {k['nama']}")

    def tambah_kunjungan(self):
        print("\n=== INPUT KUNJUNGAN BARU ===")
        nama = input("Nama Pengunjung: ")

        print("\nKategori Kunjungan TBM:")
        self.list_kategori()
        kategori = int(input("Pilih kategori (ID): "))

        tanggal = input("Tanggal (YYYY-MM-DD): ")

        kunjungan = Kunjungan(nama, kategori, tanggal)

        self.db.query("""
            INSERT INTO kunjungan (nama_pengunjung, kategori_id, tanggal)
            VALUES (%s, %s, %s)
        """, (kunjungan.nama, kunjungan.kategori_id, kunjungan.tanggal))

        self.db.commit()
        print("Data kunjungan berhasil ditambahkan!")

    def hapus_kunjungan(self):
        kid = int(input("Masukkan ID kunjungan yang ingin dihapus: "))
        self.db.query("DELETE FROM kunjungan WHERE id = %s", (kid,))
        self.db.commit()
        print("Data kunjungan berhasil dihapus!")

    def menu(self):
        while True:
            print("\n=== SISTEM KUNJUNGAN TBM ===")
            print("1. Lihat Data Kunjungan")
            print("2. Tambah Kunjungan")
            print("3. Hapus Kunjungan")
            print("4. Lihat Kategori")
            print("0. Keluar")

            pilih = input("Pilih menu: ")

            if pilih == "1":
                self.list_kunjungan()
            elif pilih == "2":
                self.tambah_kunjungan()
            elif pilih == "3":
                self.hapus_kunjungan()
            elif pilih == "4":
                self.list_kategori()
            elif pilih == "0":
                self.db.close()
                print("Keluar...")
                break
            else:
                print("Pilihan tidak valid!")
