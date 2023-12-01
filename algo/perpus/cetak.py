# import datetime
# from member import *


# def cetak_struk(nama, judul_buku, tglpinjam, tglkembali, denda):
#     # Buat tanggal dan waktu saat ini
#     now = datetime.datetime.now()

#     # Format tanggal dan waktu
#     tanggal = now.strftime("%d-%m-%Y")
#     waktu = now.strftime("%H:%M:%S")

#     # Cetak header
#     print("Struk Peminjaman Buku")
#     print("Tanggal:", tanggal)
#     print("Waktu:", waktu)

#     # Cetak data peminjam
#     print("Nama:", nama)

#     # Cetak data buku
#     print("Judul Buku:", judul_buku)
#     print("Tanggal Peminjaman:", tglpinjam)
#     print("Tanggal Deadline:", tglkembali)
#     print("Tanggal Kembali:", now.year, "-", now.month, "-", now.day)
#     print("Denda:", denda, "Rupiah")

#     # Cetak footer
#     print("---Terima Kasih Telah Meminjam Buku Ditempat Kami---")
#     print("---LUNAS---")

# # Masukan data peminjam
# nama = username

# # Masukan data buku
# ts_instace = ts()
# judul_buku = ts_instace.buku[a]
# tglpinjam = input("Masukkan tanggal peminjaman (YYYY-MM-DD): ")
# tglkembali = input("Masukkan tanggal deadline (YYYY-MM-DD): ")

# # Hitung denda
# tglskg = datetime.datetime.now()
# tglkembali = datetime.datetime.strptime(tglkembali, "%Y-%m-%d")
# selisih = tglskg - tglkembali
# hari = selisih.days
# denda = 5000 * hari

# # Cetak struk
# cetak_struk(nama, judul_buku, tglpinjam, tglkembali, denda)