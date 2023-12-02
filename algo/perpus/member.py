import datetime
import subprocess
import os
import getpass
import msvcrt
import time
from kategori import *



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
    pilihan = int(input("Apakah anda ingin |(1) meminjam buku | (2) mengembalikan buku | (3) melihat kategori| : buku(1/2/3): "))
    if pilihan == 1:
        bc = str(input("buku yang di pinjam : "))
        pj(a=bc)
    elif pilihan == 2:
        bb = str(input("buku yang di kembalikan : "))
        kmb(a=bb)
    elif pilihan == 3:
        print_buku_by_kategori()
    else:
        print("Pilihan anda tidak ada dipilihan!.")
        inti()
import json
from data import tes as ts

def kmb(a):
        with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json') as file:
            data = json.load(file)
        # Call the function to get an instance of the Tes class
        ts_instance = ts()
        usr = username

        tanggal_format = "%Y/%m/%d"
        if not data[usr]["pinjaman"]:
            print(f"{usr} tidak meminjam buku apa pun.")
        else:
            if a not in data[usr]["pinjaman"][0]["judul_buku"]:
                print(f"{usr} tidak meminjam buku apa pun.")
            else:
                if a in ts_instance.buku:
                    if ts_instance.buku[a]["tersedia"] < ts_instance.buku[a]["total"]:
                        now = datetime.datetime.today()
                        deadlinee = data[usr]["pinjaman"][0]["deadline"]
                        datetime_bukti_deadline = datetime.datetime.strptime(deadlinee, tanggal_format)
                        if datetime_bukti_deadline < now:
                            dendaw = datetime.datetime.now() - datetime_bukti_deadline 
                            print("kamu telat : ", dendaw.days, "hari")
                            jumlahd = dendaw.days * 1000
                            print(f"Rp {jumlahd}")
                            ts_instance.buku[a]["tersedia"] += 1
                            pinjaman_baru = [pinjaman for pinjaman in data[usr]["pinjaman"] if pinjaman["judul_buku"] != a]
                            data[usr]["pinjaman"] = pinjaman_baru
                        else:
                            ts_instance.buku[a]["tersedia"] += 1
                            pinjaman_baru = [pinjaman for pinjaman in data[usr]["pinjaman"] if pinjaman["judul_buku"] != a]
                            data[usr]["pinjaman"] = pinjaman_baru
                            print("terimakasih telah mengembalikan buku")
                        print(f"Buku {a} berhasil dikembalikan.")
                    else:
                        print(f"Maaf, stok buku {a} sudah penuh.")
                else:
                    print(f"Buku {a} tidak valid atau tidak sedang dipinjam.")



                with open('/backup data 2023/optional/belajar python/algo/perpus/data_buku.json', 'w') as file:
                    json.dump(ts_instance.buku, file, indent=2)
                with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json', 'w') as file:
                    json.dump(data, file, indent=2)

                # Print the updated dictionary
                for i, data in ts_instance.buku.items():
                    print(i, data["tersedia"])
        while True:
            try:
                pil = int(input("1 untuk lanjut 0 untuk log out"))
                if pil == 1:
                    inti()
                    return a
                elif pil == 0:
                    regis()
            except ValueError:
                print("inputan salah")
            return a




# from member import regis, username

def pj(a):
    with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json') as file:
        data = json.load(file)
    # Call the function to get an instance of the Tes class
    ts_instance = ts()
    usr = username
    now = datetime.datetime.now()
    deadline = now + datetime.timedelta(weeks=1)
  
    # Assuming ts_instance.buku is a dictionary where the values represent the quantity of each book
    if a in ts_instance.buku:
        if ts_instance.buku[a]["tersedia"] > 0:
            ts_instance.buku[a]["tersedia"] -= 1
            # data[usr]['pinjaman'].append(a)
            data[usr]["pinjaman"].append({
                "judul_buku": a,
                # "jumlah": jmlh,
                "bukti_waktu": now.strftime("%Y/%m/%d"),
                "deadline" : deadline.strftime("%Y/%m/%d")
                })
            print(f"Buku {a} berhasil dipinjam.")
        else:
            print(f"Maaf, stok buku {a} habis.")
    else:
        print(f"Buku {a} tidak tersedia.")

    # Print the updated dictionary
    for i, jumlah in ts_instance.buku.items():
         print(f"{i} Tersedia: {jumlah['tersedia']}")

    # Update the JSON file
    with open('/backup data 2023/optional/belajar python/algo/perpus/data_buku.json', 'w') as file:
        # Use ts_instance.buku directly to update and write to the file
        json.dump(ts_instance.buku, file, indent=2)
    with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json', 'w') as file:
        json.dump(data, file, indent=2)
    ctk()
    while True:
        try:
            pil = int(input("1 untuk lanjut 0 untuk logout"))
            if pil == 1:
                inti()
            elif pil == 0:
                regis()
        except ValueError:
            print("inputan salah")
        return a




def ctk():
    with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json') as file:
        data = json.load(file)
    
    panjang = 45

    
    nama = f"nama peminjam buku : {username}"
    status = f"status : {data[username]["sebagai"]}"
    buku = f"Buku yang dipinjam : {data[username]["pinjaman"][0]["judul_buku"]}"
    nim_nip = f"NIM/NIP{password}"
    waktu = f"Waktu pinjam : {data[username]["pinjaman"][0]["bukti_waktu"]}"
    deadline = f"Waktu deadline : {data[username]["pinjaman"][0]["deadline"]}"
    nm_p = "Perpustakaan Jurusan Teknik Elektro"
    warning = "*mohon tidak menghilangkan struk ini*"
    dld = "*melewati deadline dikenakan denda Rp1000/hari*"

    
    # Cetak struk
    data = f"""
    {"=" * panjang}

    {nama.center(panjang)}
    {nim_nip.center(panjang)}
    {buku.center(panjang)}
    {status.center(panjang)}
    {waktu.center(panjang)}
    {deadline.center(panjang)}
    {nm_p.center(panjang)}

    {warning.center(panjang)}

    {dld.center(panjang)}
    
    {"=" * panjang}
    """
    
    print(data)
    
    
    with open(username, "w") as f:
        f.write(data)

    ntpd = f"{username}"

    subprocess.run(["notepad.exe", ntpd])

    
    time.sleep(2)
    os.remove(ntpd)


regis()