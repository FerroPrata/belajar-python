
# fungsi.py

import json

class Tes:
    def __init__(self, file_path='/backup data 2023/optional/belajar python/algo/sorting/data.json'):
        try:
            with open(file_path, 'r') as file:
                self.warung = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.warung = {}
    def __inti__(self, file_path='/backup data 2023/optional/belajar python/algo/sorting/rating_user.json'):
        try:
            with open(file_path, 'r') as file:
                self.bukti = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.bukti = {}

    def save_to_file(self, file_path='/backup data 2023/optional/belajar python/algo/sorting/data.json'):
        with open(file_path, 'w') as file:
            json.dump(self.warung, file, indent=2)

    def tambah_warung(self, warung, alamat, no, rating, jarak, rekomendasi, jam_buka, jam_tutup):
        if warung not in self.warung:
            self.warung[warung] = {"alamat": alamat, "no": no, "rating": rating, "jarak": jarak, "rekomendasi" : rekomendasi, "jam buka" : jam_buka, "jam tutup" : jam_tutup}
            print(f"{warung} berhasil ditambahkan.")
        else:
            print(f"Buku dengan warung {warung} sudah ada.")
    
        

def tes():
    return Tes()