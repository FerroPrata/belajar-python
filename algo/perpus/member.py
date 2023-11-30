import datetime
import os
import getpass
import kembali
import pinjam
import msvcrt

login_reg = input("Login / Registrasi: ")
panjang = 45
def regis():
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

def inti():
    pilihan = int(input("Apakah anda ingin (1) Mengembalikan / (2) Memasukan buku (1/2): "))
    if pilihan == 1:
        bb = str(input("Mengembalikan buku"))
        kembali.kmb(a=bb)
    elif pilihan == 2:
        bc = str(input("Meminjam buku"))
        pinjam.pj(a=bc)
    else:
        print("Pilihan anda tidak ada dipilihan!.")
        inti()


regis()