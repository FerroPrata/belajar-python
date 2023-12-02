# from data import Tes

# def tambah_buku():
#     kt = "Fiksi", "Non-Fiksi", "Sains", "Komedi"
#     ts_instance = Tes()
#     judul = input("Masukkan judul buku: ")
#     total = int(input("Masukkan jumlah total stok buku: "))
#     kategori = input("Masukkan kategori buku: ")
#     if kategori not in kt:
#         print("kategori tidak tersedia di perpus ini")
#         print("Harap isi Ulang")
#         kategori(5)
#     else:
#         ts_instance.tambah_buku(judul, total, kategori)
#         ts_instance.save_to_file()
#     thn_terbit = input("Masukkan tahun terbit buku: ") #tahun terbit
#     penulis = input("Masukkan penulis buku: ") #penulis buku
#     penerbit = input("Masukkan penerbit buku: ") #penerbit
#     jumlah_hal = input("Masukkan jumlah halaman buku: ") #jumlah halaman


# # Contoh pemanggilan fungsi tambah_buku
# tambah_buku()
from data import Tes

def tambah_buku():
    kt = {"Fiksi", "Non-Fiksi", "Sains", "Komedi"}
    ts_instance = Tes()
    
    while True:
        judul = input("Masukkan judul buku: ")
        
        try:
            total = int(input("Masukkan jumlah total stok buku: "))
        except ValueError:
            print("Harap masukkan angka untuk stok buku.")
            continue

        kategori = input("Masukkan kategori buku: ")

        if kategori not in kt:
            print("Kategori tidak tersedia di perpustakaan ini")
            print("Harap isi ulang.")
            tambah_buku()
        else:
            ts_instance.tambah_buku(judul, total, kategori)
            ts_instance.save_to_file()
            break  # Keluar dari loop jika input valid
        
        try:
            thn_terbit = int(input("Masukkan tahun terbit buku: "))
        except ValueError:
            print("Harap masukkan angka untuk tahun terbit buku.")
            continue
        penulis = input("Masukkan penulis buku: ")
        penerbit = input("Masukkan penerbit buku: ")
        try:
            jumlah_hal = int(input("Masukkan jumlah halaman buku: "))
        except ValueError:
            print("Harap masukkan angka untuk jumlah halaman buku.")
            continue

# Contoh pemanggilan fungsi tambah_buku
tambah_buku()
