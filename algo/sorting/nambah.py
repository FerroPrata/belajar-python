from fungsi import Tes
from datetime import datetime

def tambah_buku():
    jam_buka_str = input("Masukkan jam buka dalam format HH:MM: ")
    try:
        jam_buka = datetime.strptime(jam_buka_str, '%H:%M').time()
        print("Jam buka berhasil diatur:", jam_buka)
    except ValueError:
        print("Format waktu tidak valid. Pastikan formatnya adalah HH:MM.")
        jam_tutup_str = input("Masukkan jam tutup dalam format HH:MM: ")
    jam_tutup_str = input("Masukkan jam tutup dalam format HH:MM: ")
    try:
        jam_tutup = datetime.strptime(jam_tutup_str, '%H:%M').time()
        print("Jam tutup berhasil diatur:", jam_tutup)
    except ValueError:
        print("Format waktu tidak valid. Pastikan formatnya adalah HH:MM.")
    jarakm = 30000
    ts_instance = Tes()
    warung = input("Nama warung : ")
    alamat = input("Masukkan alamat: ")
    no = input("masukan nomor yang dapat di hubungi : ")
    rating = float(input("masukan rating tokoh : "))
    jarak = int (input("masukan jarak tokoh dari rumah mu : "))
    rekomendasi = rating * (1 - jarak / jarakm)
    ts_instance.tambah_warung(warung, alamat, no, rating, jarak, rekomendasi, jam_buka.strftime('%H:%M'), jam_tutup.strftime('%H:%M'))
    ts_instance.save_to_file()

tambah_buku()