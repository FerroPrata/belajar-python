import datetime
import os
import getpass
import msvcrt



login_reg = input("Login / Registrasi: ")
panjang = 45
def regis():
    global username
    while True:
        if login_reg == "login" or login_reg == "Login":
            break
        else:
            username = input("Masukkan Nama : ")
            password = input("Masukkan NIM : ")
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
                data = json.load(file)
                usr = username
                new_user = {"nama": str(usr), "pinjaman": []}
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
    pilihan = int(input("Apakah anda ingin (1) Mengembalikan / (2) Memasukan buku (1/2): "))
    if pilihan == 1:
        bb = str(input("Mengembalikan buku"))
        kmb(a=bb)
    elif pilihan == 2:
        bc = str(input("Meminjam buku"))
        pj(a=bc)
    else:
        print("Pilihan anda tidak ada dipilihan!.")
        inti()
import json
from data import tes as ts
# from member import regis, username


def kmb(a):
    with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json') as file:
        data = json.load(file)
    # Call the function to get an instance of the Tes class
    ts_instance = ts()
    usr = username

    if a in ts_instance.buku:
        if ts_instance.buku[a]["tersedia"] < ts_instance.buku[a]["total"]:
            ts_instance.buku[a]["tersedia"] += 1
            data[usr]['pinjaman'].remove(a)
            print(f"Buku {a} berhasil dikembalikan.")
        else:
            print(f"Maaf, stok buku {a} sudah penuh.")
    else:
        print(f"Buku {a} tidak valid atau tidak sedang dipinjam.")

    # Save the updated data to the file
    with open('/backup data 2023/optional/belajar python/algo/perpus/data_buku.json', 'w') as file:
        # Use ts_instance.buku directly to update and write to the file
        json.dump(ts_instance.buku, file, indent=2)
    with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json', 'w') as file:
        json.dump(data, file, indent=2)

    # Print the updated dictionary
    for i, data in ts_instance.buku.items():
        print(i, data["tersedia"])


# from member import regis, username

def pj(a):
    with open('/backup data 2023/optional/belajar python/algo/perpus/bukti_user.json') as file:
        data = json.load(file)
    # Call the function to get an instance of the Tes class
    ts_instance = ts()
    usr = username
  
    # Assuming ts_instance.buku is a dictionary where the values represent the quantity of each book
    if a in ts_instance.buku:
        if ts_instance.buku[a]["tersedia"] > 0:
            ts_instance.buku[a]["tersedia"] -= 1
            data[usr]['pinjaman'].append(a)
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





regis()