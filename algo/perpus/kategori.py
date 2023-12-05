from data import Tes

def print_buku_by_kategori():
    ts_instance = Tes()
    kategori_list = ["Fiksi", "Non-Fiksi", "Sains", "Komedi"]
    inp_kategori = input("Masukkan kategori buku: ")

    if inp_kategori in kategori_list:
        hasil_filter = ts_instance.filter_buku_by_kategori(inp_kategori)
        if hasil_filter:
            print(f"\nBuku dengan kategori '{inp_kategori}':")
            for judul, buku_info in hasil_filter.items():
                print(f"Judul: {judul}, Tersedia: {buku_info['tersedia']}")
        else:
            print("Tidak ada buku dengan kategori tersebut.")
    else:
        print("Maaf, kategori buku '{inp_kategori}' yang Anda masukkan tidak tersedia.")
    while True:
        pilihan = input("1. Untuk Mencari lagi 2. Untuk kembali\nPilihan: ")
        if pilihan == '1':
            print_buku_by_kategori()
            break
        elif pilihan == '2':
            print("kembali")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
            
        
        
        
def print_buku_by_tahun():
    ts_instance = Tes()
    kategori_list = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    inp_tahun = int(input("Masukkan tahun buku: "))

    if inp_tahun in kategori_list:
        hasil_filter = ts_instance.filter_buku_by_tahun(inp_tahun)

        if hasil_filter:
            print(f"\nBuku dengan tahun '{inp_tahun}':")
            for judul, buku_info in hasil_filter.items():
                print(f"Judul: {judul}, Tersedia: {buku_info['tersedia']}")
        else:
            print("Tidak ditemukan buku di tahun tersebut.")
    else:
        print("Maaf, tahun buku '{inp_tahun}' yang Anda masukkan tidak tersedia.")
    while True:
        pilihan = input("1. Untuk Mencari lagi 2. Untuk kembali\nPilihan: ")
        if pilihan == '1':
            print_buku_by_tahun()
            break
        elif pilihan == '2':
            print("kembali")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")



def print_buku_by_nama():
    ts_instance = Tes()
    nama_pe = (input("Masukkan nama penulis buku: "))

    hasil_filter = None

    if not nama_pe:
        print("Maaf, nama tidak dapat ditemukan.")
        print_buku_by_nama()
        return nama_pe
    else:
        hasil_filter = ts_instance.filter_buku_by_nama_p(nama_pe)
        if hasil_filter:
            print(f"\nPenulis Buku dengan nama '{nama_pe}':")
            for judul, buku_info in hasil_filter.items():
                print(f"Judul: {judul} \nTersedia: {buku_info['tersedia']}\n")
        else:
          print("Penulis buku tidak ditemukan.")

    while True:
        try:
            pilihan = input("1. Untuk Mencari lagi 2. Untuk kembali\nPilihan: ")
            if pilihan == '1':
                print_buku_by_nama()
            elif pilihan == '2':
                print("kembali")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
        except ValueError:
            print("Input salah. Masukkan angka 1 atau 2.")