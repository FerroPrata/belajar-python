import json
import prettytable

def cek_g():    
    with open("/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json", "r") as f:
        data = json.load(f)

    tabel = prettytable.PrettyTable()
    tabel.field_names = ["Nama", "Status", "Judul buku", "Bukti waktu", "Deadline", "Kode struk"]

    for nama, detail in data.items():
        if detail["pinjaman"]:
            pinjaman = detail["pinjaman"][0]
            tabel.add_row([nama, detail["sebagai"], pinjaman["judul_buku"], pinjaman["bukti_waktu"], pinjaman["deadline"], pinjaman["kode_struk"]])


    print(tabel)

    while True:
        pilihan = input("\n1. Untuk Mencari lagi 2. Untuk kembali\nPilihan: ")
        if pilihan == '1':
            cek_g()
        elif pilihan == '2':
            print("kembali")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

def cek_b():
    with open("/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json", "r") as f:
        data = json.load(f)
    with open("/backup data 2023/optional/belajar python/algo/perpus/data_buku.json", "r") as f:
        dataa = json.load(f)
    hasil = list(dataa.keys())

    book_to_check = input("masukan buku : ")
  # Pencarian pengguna yang meminjam buku tertentu
    if book_to_check in hasil:
        print(f"peminjam buku {book_to_check} : ", end="")
        for username, user_data in data.items():
          if user_data["pinjaman"]:
            for pinjaman in user_data["pinjaman"]:
              if pinjaman["judul_buku"].lower() == book_to_check.lower():
                print(f"\'{username}\'", end=" ")
                
    else:
        print("buku tidak dipinjam siapapun")

    while True:
        pilihan = input("\n\n1. Untuk Mencari lagi 2. Untuk kembali\nPilihan: ")
        if pilihan == '1':
            cek_b()
        elif pilihan == '2':
            print("kembali")
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih 1 atau 2.")

