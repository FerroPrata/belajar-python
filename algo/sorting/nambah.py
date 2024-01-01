from fungsi import Tes

def tambah_buku():
    ts_instance = Tes()
    warung = input("Nama warung")
    alamat = input("Masukkan judul buku: ")
    no = input("masukan nomor yang dapat di hubungi")
    ts_instance.tambah_warung(warung, alamat, no)
    ts_instance.save_to_file()

tambah_buku()