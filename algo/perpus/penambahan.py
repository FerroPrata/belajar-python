from data import Tes

def tambah_buku():
    kt = "Fiksi", "Non-Fiksi", "Sains", "Komedi"
    ts_instance = Tes()
    #kode = input("Kode untuk buku:\n A = Fiksi\n B = Non-Fiksi\n C = Sains\n D = Komedi\n Masukkan kode buku:")
    judul = input("Masukkan judul buku: ")
    while True:
        try:
            total = int(input("Masukkan jumlah total stok buku: "))
            if not total:
                ("masukan angka")
            else:
                break
        except ValueError:
                    print("masukan angka")
    while True:
        try:
            kategori = input("Masukkan kategori buku: ")
            if kategori in kt:
                break
            else:
                ("kategori tidak tersedi")
        except ValueError:
                    print("kategori tidak tersedi")
    while True:
        try:
            thn_terbit = int(input("Masukkan tahun terbit buku: "))
            if not thn_terbit:
                ("masukan angka")
            else:
                break
        except ValueError:
                    print("masukan angka")
    penulis = input("Masukkan penulis buku: ") #penulis buku
    penerbit = input("Masukkan penerbit buku: ") #penerbit
    while True:
        try:
            jumlah_hal = int(input("Masukkan jumlah halaman buku: "))
            if not jumlah_hal:
                ("masukan angka")
            else:
                break
        except ValueError:
                    print("masukan angka")
    #ts_instance.tambah_buku(kode, judul, total, kategori, thn_terbit, penulis, penerbit, jumlah_hal)
    ts_instance.save_to_file()

