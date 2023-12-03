# data.py

import json

class Tes:
    def __init__(self, file_path='/backup data 2023/optional/belajar python/algo/perpus/data_buku.json'):
        try:
            with open(file_path, 'r') as file:
                self.buku = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.buku = {}
    def __inti__(self, file_path='/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json'):
        try:
            with open(file_path, 'r') as file:
                self.bukti = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.bukti = {}

    def save_to_file(self, file_path='/backup data 2023/optional/belajar python/algo/perpus/data_buku.json'):
        with open(file_path, 'w') as file:
            json.dump(self.buku, file, indent=2)

    def tambah_buku(self, judul, total, kategori, thn_terbit, penulis, penerbit, jumlah_hal):
        if judul not in self.buku:
            self.buku[judul] = {"total": total, "tersedia": total, "kategori": kategori, "tahun_terbit": thn_terbit, "Penulis": penulis, "Penerbit": penerbit, "jumlah_halaman": jumlah_hal }
            print(f"Buku {judul} berhasil ditambahkan.")
        else:
            print(f"Buku dengan judul {judul} sudah ada.")
    
    def filter_buku_by_kategori(self, kategori):
        hasil_filter = {judul: buku_info for judul, buku_info in self.buku.items() if buku_info.get("kategori") == kategori}
        return hasil_filter
    
    def filter_buku_by_tahun(self, tahun):
        hasil_filter = {judul: buku_info for judul, buku_info in self.buku.items() if buku_info.get("tahun_terbit") == tahun}
        return hasil_filter
    
    def filter_buku_by_nama_p(self, nama_p):
      hasil_filter = {judul: buku_info for judul, buku_info in self.buku.items() if buku_info.get("Penulis") == nama_p}
      return hasil_filter
        

def tes():
    return Tes()