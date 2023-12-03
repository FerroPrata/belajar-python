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

