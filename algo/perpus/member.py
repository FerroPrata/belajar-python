import datetime
import subprocess
import os
import getpass
import msvcrt
import time
from kategori import *
from tes import *



login_reg = input("Login / Registrasi: ")
panjang = 45
def regis():
    global sbg
    global password
    global username
    while True:
        if login_reg == "login" or login_reg == "Login":
            break
        else:
            tp = ["dosen", "mahasiswa", "tamu"]
            username = input("Masukkan Nama : ")
            password = input("Masukkan NIM/NIP : ")
            while True:
                try:
                    sbg = input("status dosen/mahasiswa/tamu: ")
                    if sbg in tp:
                        break
                    else:
                        ("status tidak tersedia")
                except ValueError:
                    print("status tidak tersedia")

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
            with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json') as file:
                try:
                    data = json.load(file)
                except json.decoder.JSONDecodeError:
                # Tangani jika file JSON kosong atau tidak sesuai
                    data = {}
                usr = username
                new_user = {"nama": str(usr), "pinjaman": [], "sebagai": str(sbg)}
                data.update({str(usr): new_user})
            with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json', 'w') as file:
                json.dump(data, file, indent=2)
            print('')
            print("Data telah disimpan dalam Database")
            break

    max_attempts = 3
    attempts = 0
    print("Program Login Perpustakaan".center(panjang))

    with open("user_data.txt", "r") as file:
        lines = file.readlines()

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
        if any(line.strip() == f"{username},{password},{pin}" for line in lines):
            print()
            print("Login berhasil!")
            inti()
        else:
            print("Login gagal. Coba lagi.")
            attempts += 1
            if attempts == max_attempts:
                print("Anda telah melebihi batas percobaan login.")
    return username

def inti():
    global bc
    global bb
    pilihan = int(input("Apakah anda ingin |(1) meminjam buku | (2) mengembalikan buku | (3) melihat kategori| : buku(1/2/3): "))
    if pilihan == 1:
        bc = str(input("buku yang di pinjam : "))
        pj(a=bc)
    elif pilihan == 2:
        kmb()
    elif pilihan == 3:
        print_buku_by_kategori()
    else:
        print("Pilihan anda tidak ada dipilihan!.")
        inti()
import json
from data import tes as ts



def kmb():
    with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json') as file:
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

    with open('/backup data 2023/optional/belajar python/algo/perpus/data_buku.json', 'w') as file:
        json.dump(ts_instance.buku, file, indent=2)

    with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json', 'w') as file:
        json.dump(data, file, indent=2)

    # Print the updated dictionary
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




# from member import regis, username

def pj(a):
    with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json') as file:
        data = json.load(file)

    ts_instance = Tes()  # Creating an instance of the Tes class

    usr = username
    now = datetime.datetime.now()
    deadline = now + datetime.timedelta(weeks=1)

    # Split the input by comma and remove leading/trailing whitespaces
    books_to_borrow = [book.strip() for book in a.split(',')]

    for book in books_to_borrow:
        if book in ts_instance.buku:
            if ts_instance.buku[book]["tersedia"] > 0:
                ts_instance.buku[book]["tersedia"] -= 1
                stri = generate_unique_id()
                data[usr]["pinjaman"].append({
                    "judul_buku": book,
                    "bukti_waktu": now,
                    "deadline": deadline,
                    "kode_struk": stri
                })
                print(f"Buku {book} berhasil dipinjam.")
            else:
                print(f"Maaf, stok buku {book} habis.")
        else:
            print(f"Buku {book} tidak tersedia.")

    # Print the updated dictionary
    for i, jumlah in ts_instance.buku.items():
        print(f"{i} Tersedia: {jumlah['tersedia']}")

    # Update the JSON files
    with open('/backup data 2023/optional/belajar python/algo/perpus/data_buku.json', 'w') as file:
        json.dump(ts_instance.buku, file, indent=2)
    with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json', 'w') as file:
        json.dump(data, file, indent=2)

    ctk()
    while True:
        try:
            pil = int(input("1 untuk lanjut/ 0 untuk logout"))
            if pil == 1:
                inti()
            elif pil == 0:
                regis()
        except ValueError:
            print("inputan salah")



def ctk():
    with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json') as file:
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