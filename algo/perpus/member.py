import datetime
import os
import getpass
import kembali
import pinjam

login_reg = input("Login / Registrasi:")
panjang = 45
def regis():
    while True:
        if login_reg == "login":
            break
        else:
            username = input("Masukkan username regis:")
            password = input("Masukkan password regis:")
            with open("user_data.txt", "a") as file:
                file.write(f"{username},{password}\n")
            print("Data telah disimpan dalam Database")
            break

    max_attempts = 3
    attempts = 0
    print("Program Login Kasir".center(panjang))

    while attempts < max_attempts:
        username = input("Masukkan username : ")
        password = input("Masukkan password : ")
        if username == f"{username}" and password == f"{password}":
            print("Login berhasil!")
            inti()
        else:
            print("Login gagal. Coba lagi.")
            attempts + 1

    if attempts == max_attempts:
        print("Anda telah melebihi batas percobaan login.")



def inti():
    pilihan = int(input("pilih"))
    if pilihan == 1:
        bb = str(input("masukan buku"))
        kembali.kmb(a=bb)
    elif pilihan == 2:
        bc = str(input("masukan buku"))
        pinjam.pj(a=bc)


regis()