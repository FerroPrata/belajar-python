from patch1 import *
from patch2 import *
from patch3 import *

import json
import datetime
from prettytable import PrettyTable

with open("D:/backup data 2023/optional/belajar python/algo/sorting/data.json", "r") as f:
        dataa = json.load(f)
def main():
    global nama
    nama = input("masukan nama anda : ")
    data = list(dataa.items())        
    now = datetime.datetime.now().time()

    print(f"selamat datang {nama}", "\n")
    table = PrettyTable()
    table.field_names = ["Nama warung", "status", "jam buka", "jam tutup"]
    for buku in data:
        jam_buka = datetime.datetime.strptime(buku[1]['jam buka'], "%H:%M").time()
        jam_tutup = datetime.datetime.strptime(buku[1]['jam tutup'], "%H:%M").time()
        if jam_buka <= now <= jam_tutup:
            status = "buka"
        else:
            status = "tutup"
        table.add_row([buku[0], status, buku[1]['jam buka'], buku[1]['jam tutup']])
    print(table)
    min()

def min():
    pilihan = int(input("|(1) melihat rating warung       |\n|(2) melihat jarak terdekat      |\n|(3) rekomendasi untuk anda      |\n|(0) exit                        |\n masukan pilihan : "))
    if pilihan == 1:
        print()
        warung_sorting()
        print()
        table = PrettyTable()
        welcome = f"hai {nama}"
        table.field_names = [welcome]
        table.add_row(["ini urutan rating warung untuk anda"])
        print(table)
        coba1()
        min()
        return
    elif pilihan == 2:
        print()
        buble_sort()
        print()
        table = PrettyTable()
        welcome = f"hai {nama}"
        table.field_names = [welcome]
        table.add_row(["ini urutan jarak terdekat warung untuk anda"])
        print(table)
        coba()
        min()
        return
    elif pilihan == 3:
        print()
        table = PrettyTable()
        welcome = f"hai {nama}"
        table.field_names = [welcome]
        table.add_row(["ini rekomendasi warung untuk anda"])
        print(table)
        selection_sort()
        min()
        return
    elif pilihan == 0:
        return
    else:
        print("Pilihan anda tidak ada dipilihan!.")
        main()
        return
main()