import datetime
import subprocess
import os
import msvcrt
import time
from kategori import *
from random_char import *
from p_pinjam import *
from penambahan import *
from hapus import *



# login dan register 
panjang = 45
def regis():
    login_reg = input("Login / Registrasi: ")
    global sbg
    global password
    global username
    while True:
        if login_reg == "login" or login_reg == "Login":
            break
        else:
            username = input("Masukkan Nama : ")
            while True:
                try:
                    password = input("Masukkan NIM/NIP: ")
                    if password.isdigit():
                        password = int(password)

                        tahun = [1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
                        bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                        tanggal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

                        # Memisahkan tahun, bulan, dan tanggal dari NIM/NIP
                        tahun_nip = int(str(password)[:14])
                        bulan_nip = (password % 10000) // 100
                        tanggal_nip = password % 100

                        if len(str(password)) == 10:
                            sbg = "mahasiswa"
                            break
                        elif len(str(password)) >= 18 and len(str(password)) <= 19:
                            # Menambahkan kondisi untuk memastikan enam digit pertama adalah tahun, bulan, dan tanggal yang valid
                            if tahun_nip >= tahun[0] and bulan_nip in bulan and tanggal_nip in tanggal:
                                sbg = "dosen"
                                break
                            else:
                                print("salah")
                        elif len(str(password)) < 10:
                            sbg = "tamu"
                            break
                        else:
                            print("Format NIM/NIP tidak valid.")
                    else:
                        print("NIM/NIP harus berupa angka.")
                except ValueError:
                    print("NIM/NIP tidak tersedia")
            print("Masukkan PIN:", end='', flush=True)#perubahan
            pin = ""
            while True:
                char = msvcrt.getch().decode('utf-8')
                if char == '\r':
                    break
                pin += char
                print('*', end='', flush=True)
            with open("user_data.txt", "a") as file:
                file.write(f"{username},{password},{pin}\n")
            with open('\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Project 1\\bukti_user.json') as file:
                try:
                    data = json.load(file)
                except json.decoder.JSONDecodeError:
                # Tangani jika file JSON kosong atau tidak sesuai
                    data = {}
                usr = username
                new_user = {"nama": str(usr), "pinjaman": [], "sebagai": str(sbg)}
                data.update({str(usr): new_user})
            with open('\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Project 1\\bukti_user.json', 'w') as file:
                json.dump(data, file, indent=2)
            print('')
            print("Data telah disimpan dalam Database")
            break

    max_attempts = 3
    attempts = 0
    print("Program Login Perpustakaan".center(panjang))
    with open("user_data.txt", "r") as file:
        lines = file.readlines()
    
    admin_username = "admin"
    admin_password = "admin"
    kode = "admin"

    while attempts < max_attempts:
        username = input("Masukan Nama : ")
        password = input("Masukan NIM : ")
        print("Masukkan PIN:", end='', flush=True)#perubahan
        pin = ""
        while True:
            char = msvcrt.getch().decode('utf-8')
            if char == '\r':
                break
            pin += char
            print('*', end='', flush=True)
        if username == admin_username and password == admin_password and pin == kode:
            print("\nHak istimewa admin diberikan.")
            admin()
        else:
            if any(line.strip() == f"{username},{password},{pin}" for line in lines):
                print()
                print(f"\n        Login berhasil")
                print(f"    Selamat Datang {username}!\n")
                inti()
            else:
                print("Login gagal. Coba lagi.")
                attempts += 1
                if attempts == max_attempts:
                    print("Anda telah melebihi batas percobaan login.")
    return username

# main menu 
def inti():
    ts_instance = Tes()
    global bc
    global bb
    pilihan = int(input("|(1) meminjam buku             |\n|(2) mengembalikan buku        |\n|(3) filter kategori buku      |\n|(4) filter tahun terbit buku  |\n|(5) filter nama penulis buku  |\n|(6) melihat buku              |\n|(0) Logout                    |\n\n pilih(1/2/3/4/5/6/0): "))
    if pilihan == 1:
        bc = str(input("Masukkan kode buku yang di pinjam : "))
        pj(a=bc)
    elif pilihan == 2:
        kmb()
    elif pilihan == 3:
        print_buku_by_kategori()
        inti()
    elif pilihan == 4:
        print_buku_by_tahun()
        inti()
    elif pilihan == 5:
        print_buku_by_nama()
        inti()
    elif pilihan == 6:
        for i, data in ts_instance.buku.items():
            print(f"\nbuku : {i}\nkode buku : {data["kode"]}\njumlah tersedia : {data["tersedia"]}\n")
        inti()
    elif pilihan == 0:
        regis()
        return
    else:
        print("Pilihan anda tidak ada dipilihan!.")
        inti()
import json
from data import tes as ts


# hak istimewa admin 
def admin():
    ts_instance = Tes()
    global bc
    global bb
    pilihan = int(input("\n|(1) pendataan buku             |\n|(2) pemantauan user            |\n|(3) pemantauan pinjaman        |\n|(4) penghapusan buku           |\n|(0) Logout                     |\n pilih(1/2/3/4/0): "))
    if pilihan == 1:
        tambah_buku()
        admin()
    elif pilihan == 2:
        cek_g()
        admin()
    elif pilihan == 3:
        cek_b()
        admin()
    elif pilihan == 4:
        hapus_buku_dan_pinjaman()
        admin()
    elif pilihan == 0:
        regis()
        return
    else:
        print("Pilihan anda tidak ada dipilihan!.")
        inti()


# fungsi pengembalian

def kmb():
    with open('\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Project 1\\bukti_user.json') as file:
        data = json.load(file)

    kode_struk_input = input("Masukkan kode struk : ")
    list_kode_struk = kode_struk_input.split(',')
    ts_instance = Tes()
    usr = username
    tanggal_format = "%Y/%m/%d"

    if not data[usr]["pinjaman"]:
        print(f"{usr} tidak meminjam buku apa pun.")
    else:
        for b in list_kode_struk:
            buku_peminjaman = next((pinjaman for pinjaman in data[usr]["pinjaman"] if pinjaman["kode_struk"] == b), None)
            if not buku_peminjaman:
                print(f"{usr} tidak meminjam buku dengan kode struk {b}.")
            else:
                judul_buku = buku_peminjaman["judul_buku"]

                if judul_buku in ts_instance.buku:
                    if ts_instance.buku[judul_buku]["tersedia"] < ts_instance.buku[judul_buku]["total"]:
                        now = datetime.datetime.today()
                        deadlinee = buku_peminjaman["deadline"]
                        datetime_bukti_deadline = datetime.datetime.strptime(deadlinee, tanggal_format)

                        if datetime_bukti_deadline < now:
                            dendaw = datetime.datetime.now() - datetime_bukti_deadline
                            print("kamu telat : ", dendaw.days, "hari")
                            jumlahd = dendaw.days * 1000
                            print(f"Rp {jumlahd}")

                        ts_instance.buku[judul_buku]["tersedia"] += 1
                        pinjaman_baru = [pinjaman for pinjaman in data[usr]["pinjaman"] if pinjaman["kode_struk"] != b]
                        data[usr]["pinjaman"] = pinjaman_baru

                        print(f"Buku {judul_buku} dengan kode struk {b} berhasil dikembalikan.")
                    else:
                        print(f"Maaf, stok buku {judul_buku} sudah penuh.")
                else:
                    print(f"Buku {judul_buku} tidak valid atau tidak sedang dipinjam.")

    with open('\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Project 1\\data_buku.json', 'w') as file:
        json.dump(ts_instance.buku, file, indent=2)

    with open('\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Project 1\\bukti_user.json', 'w') as file:
        json.dump(data, file, indent=2)
    for i, data in ts_instance.buku.items():
        print(i, data["tersedia"])

        while True:
            try:
                pil = int(input("1 untuk lanjut/ 0 untuk logout"))
                if pil == 1:
                    inti()
                elif pil == 0:
                    regis()
            except ValueError:
                print("inputan salah")




# fungsi peminjaman buku 

# def pj(a):
#     with open('\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Project 1\\bukti_user.json') as file:
#         data = json.load(file)

#     ts_instance = Tes()  

#     usr = username
#     now = datetime.datetime.now()
#     deadline = now + datetime.timedelta(weeks=1)

#     kode_buku_dipinjam = [kode.strip() for kode in a.split(',')]

#     for kode in kode_buku_dipinjam:
#         buku = next((judul for judul, info in ts_instance.buku.items() if info["kode"] == kode), None)

#         if buku and ts_instance.buku[buku]["tersedia"] > 0:
#             ts_instance.buku[buku]["tersedia"] -= 1
#             stri = generate_unique_id()
#             data[usr]["pinjaman"].append({
#                 "judul_buku": buku,
#                 "bukti_waktu": now.strftime("%Y/%m/%d5"),
#                 "deadline": deadline.strftime("%Y/%m/%d"),
#                 "kode_struk": stri
#             })
#             print(f"Buku dengan kode {kode} berhasil dipinjam.")
#         elif buku:
#             print(f"Maaf, stok buku dengan kode {kode} habis.")
#         else:
#             print(f"Buku dengan kode {kode} tidak tersedia.")

#     for i, jumlah in ts_instance.buku.items():
#         print(f"{i} Tersedia: {jumlah['tersedia']}")

#     with open('\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Project 1\\data_buku.json', 'w') as file:
#         json.dump(ts_instance.buku, file, indent=2)
#     with open('\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Project 1\\bukti_user.json', 'w') as file:
#         json.dump(data, file, indent=2)

#     ctk()
#     while True:
#         try:
#             pil = int(input("1 untuk lanjut/ 0 untuk logout"))
#             if pil == 1:
#                 inti()
#             elif pil == 0:
#                 regis()
#         except ValueError:
#             print("inputan salah")



def ctk():
    with open('\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Project 1\\bukti_user.json') as file:
        data = json.load(file)

    if username in data:
        panjang = 45
        n = len(data[username]["pinjaman"])

        for i in range(n):
            nama = f"nama peminjam buku : {username}"
            status = f"status : {data[username]['sebagai']}"
            buku = f"Buku yang dipinjam : {data[username]['pinjaman'][i]['judul_buku']}"
            nim_nip = f"NIM/NIP{password}"
            waktu = f"Waktu pinjam : {data[username]['pinjaman'][i]['bukti_waktu']}"
            deadline = f"Waktu deadline : {data[username]['pinjaman'][i]['deadline']}"
            nm_p = "Perpustakaan Jurusan Teknik Elektro"
            warning = "*mohon tidak menghilangkan struk ini*"
            dld = "*melewati deadline dikenakan denda Rp1000/hari*"
            ids = f"kode struk : {data[username]['pinjaman'][i]['kode_struk']}"

            info = f"""
            {"=" * panjang}

            {nama.center(panjang)}
            {status.center(panjang)}
            {nim_nip.center(panjang)}
            {buku.center(panjang)}
            {waktu.center(panjang)}
            {deadline.center(panjang)}
            {nm_p.center(panjang)}

            {warning.center(panjang)}

            {dld.center(panjang)}

            {ids.center(panjang)}

            {"=" * panjang}
            """

            print(info)

            with open(f"{username}-{i}.txt", "w") as f:
                f.write(info)

            subprocess.Popen(["notepad.exe", f"{username}-{i}.txt"])

            time.sleep(2)
            os.remove(f"{username}-{i}.txt")
    else:
        print(f"User {username} tidak ditemukan.")


regis()
