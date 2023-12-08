import json


def hapus_buku_dan_pinjaman():
    with open("/backup data 2023/optional/belajar python/algo/perpus/data_buku.json", "r") as file_buku:
        data_buku = json.load(file_buku)
    with open("/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json", "r") as file_user:
        data_user = json.load(file_user)

    daftar_buku = list(data_buku.keys())
    print("Daftar Buku:")
    for buku in daftar_buku:
        print("-", buku)

    buku_yang_akan_dihapus = input("Masukkan judul buku yang ingin dihapus: ")
    if buku_yang_akan_dihapus not in daftar_buku:
        print("Buku tidak ditemukan.")
    else:
        del data_buku[buku_yang_akan_dihapus]
        print(f"Buku {buku_yang_akan_dihapus} telah dihapus.")

        for pengguna in data_user:
            pinjaman_pengguna = data_user[pengguna]["pinjaman"]
            for pinjaman in pinjaman_pengguna:
                if pinjaman["judul_buku"] == buku_yang_akan_dihapus:
                    pinjaman_pengguna.remove(pinjaman)
                    print(f"Buku {buku_yang_akan_dihapus} juga dihapus dari daftar pinjaman pengguna {pengguna}.")

        with open("/backup data 2023/optional/belajar python/algo/perpus/data_buku.json", 'w') as file_buku:
            json.dump(data_buku, file_buku, indent=2)

        with open("/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json", 'w') as file_user:
            json.dump(data_user, file_user, indent=2)

    while True:
        pilihan = input("\n1. Untuk Mencari lagi 2. Untuk kembali\nPilihan: ")
        if pilihan == '1':
            hapus_buku_dan_pinjaman()
        elif pilihan == '2':
            print("kembali")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")


