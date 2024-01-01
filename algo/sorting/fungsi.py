
# fungsi.py

import json

class Tes:
    def __init__(self, file_path='/backup data 2023/optional/belajar python/algo/sorting/data.json'):
        try:
            with open(file_path, 'r') as file:
                self.buku = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.buku = {}
    def __inti__(self, file_path='/backup data 2023/optional/belajar python/algo/sorting/rating_user.json'):
        try:
            with open(file_path, 'r') as file:
                self.bukti = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.bukti = {}

    def save_to_file(self, file_path='/backup data 2023/optional/belajar python/algo/sorting/data.json'):
        with open(file_path, 'w') as file:
            json.dump(self.buku, file, indent=2)

    def tambah_warung(self, alamat, warung, no):
        if warung not in self.buku:
            self.buku[warung] = {"alamat": alamat, "no": no}
            print(f"{warung} berhasil ditambahkan.")
        else:
            print(f"Buku dengan warung {warung} sudah ada.")
    
    def filter_buku_by_kategori(self, kategori):
        hasil_filter = {judul: buku_info for judul, buku_info in self.buku.items() if buku_info.get("kategori") == kategori}
        return hasil_filter
    
    def filter_buku_by_tahun(self, tahun):
        hasil_filter = {judul: buku_info for judul, buku_info in self.buku.items() if buku_info.get("tahun_terbit") == tahun}
        return hasil_filter
    
    def filter_buku_by_nama_p(self, nama_p):
        nama_p = nama_p.lower() #Ubah input menggunakan lower
        hasil_filter = {judul: buku_info for judul, buku_info in self.buku.items() if nama_p in buku_info.get("Penulis").lower()} #Menggunakan fungsi in pada buku_info.get dan menambah fungsi lower diakhir
        return hasil_filter
        

def tes():
    return Tes()