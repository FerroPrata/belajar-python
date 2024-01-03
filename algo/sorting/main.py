import json
import time
from prettytable import PrettyTable
import datetime
from patch1 import *
from patch2 import *
from patch3 import *

nama = input("Masukkan Nama Anda: ")

print(f"Selamat Datang {nama}")
print("Mau makan apa hari ini?")
def format_time(time_str):
    return datetime.datetime.strptime(time_str, "%H:%M").replace(tzinfo=datetime.timezone.utc).time()

def get_status(jam_buka, jam_tutup, now):
    jam_buka = format_time(jam_buka)
    jam_tutup = format_time(jam_tutup)
    if jam_buka <= now <= jam_tutup:
        return "buka"
    else:
        return "tutup"
with open("\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Tugas AKhir\\2\\data.json", "r") as f:
    dataa = json.load(f)
tabel = list(zip(dataa.keys(), [buku["rating"] for buku in dataa.values()]))
table1 = PrettyTable()
table1.field_names = ["nama warung", "rating"]
for buku in tabel:
    table1.add_row(buku)
print(table1)




def main():
    with open("\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Tugas AKhir\\2\\data.json", "r") as f:
        dataa = json.load(f)

    rating = [buku["rating"] for buku in dataa.values()]
    nama = [buku for buku in dataa.keys()]
    tutup = [buku["jam tutup"] for buku in dataa.values()]

    import datetime
    now = datetime.datetime.now().time()

    status_awal = []

    for restaurant, info in dataa.items():
        jam_buka = datetime.datetime.strptime(info["jam buka"], "%H:%M").replace(tzinfo=datetime.timezone.utc).time()
        jam_tutup = datetime.datetime.strptime(info["jam tutup"], "%H:%M").replace(tzinfo=datetime.timezone.utc).time()

        if jam_buka <= now <= jam_tutup:
            status = "buka"
        else:
            status = "tutup"

        status_awal.append(status)

    data = list(dataa.items())

    while True:
        pilihan = input("Pilih jenis sorting (1: berdasarkan rating, 2: berdasarkan jarak, 3: berdasarkan rekomendasi, 0: keluar): ")

        if pilihan == "1":
            sorted_data = insertion_sort(data)
            print("\nWarung setelah di sorting by rating")
            table = PrettyTable()
            table.field_names = ["nama warung", "rating", "status", "jam tutup"]
            for buku in sorted_data:
                jam_buka = datetime.datetime.strptime(buku[1]['jam buka'], "%H:%M").time()
                jam_tutup = datetime.datetime.strptime(buku[1]['jam tutup'], "%H:%M").time()
                if jam_buka <= now <= jam_tutup:
                    status = "buka"
                else:
                    status = "tutup"
                table.add_row([buku[0], buku[1]['rating'], status, buku[1]['jam tutup']])
            print(table)
        elif pilihan == "2":
            sorted_data = bubble_sort()
            print("\nWarung setelah di sorting by jarak")
            table = PrettyTable()
            table.field_names = ["nama warung", "jarak"]
            for buku in sorted_data:
                table.add_row([buku[0], buku[1]['jarak']])
            print(table)
        elif pilihan == "3":
            selection_sort(data)
            table = PrettyTable()
            table.field_names = ["Nama Rumah Makan", "Rekomendasi"]
            for nama, info in data:
                table.add_row([nama, info['rekomendasi']])
            print(table)
        elif pilihan == "0":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Harap pilih 1, 2, 3, atau 0.")

if __name__ == "__main__":
    main()
