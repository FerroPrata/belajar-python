import json
import time
from prettytable import PrettyTable
import datetime

def format_time(time_str):
    return datetime.datetime.strptime(time_str, "%H:%M").replace(tzinfo=datetime.timezone.utc).time()

def get_status(jam_buka, jam_tutup, now):
    jam_buka = format_time(jam_buka)
    jam_tutup = format_time(jam_tutup)
    if jam_buka <= now <= jam_tutup:
        return "buka"
    else:
        return "tutup"

def warung_sorting():
    with open("D:/backup data 2023/optional/belajar python/algo/sorting/data.json", "r") as f:
        dataa = json.load(f)

    now = datetime.datetime.now().time()
    data = list(dataa.items())

    a = 0
    waktuM = time.time()
    for i in range(1, len(data)):
        key_item = data[i]
        j = i - 1
        while j >= 0 and data[j][1]["rating"] < key_item[1]["rating"]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key_item
        print(f"step ke-{a} : {[buku[1]['rating'] for buku in data]}, iterasi ke-{i}")
        a += 1

    waktuS = time.time()
    waktuA = waktuS - waktuM
    print(f'Waktu : {waktuA:.6f}')

    print("\nWarung sebelum di sorting")
    tabel = list(zip(dataa.keys(), [buku["rating"] for buku in dataa.values()]))

    table1 = PrettyTable()
    table1.field_names = ["nama warung", "rating"]
    for buku in tabel:
        table1.add_row(buku)
    print(table1)

    print("\nWarung setelah di sorting by rating")
    table = PrettyTable()
    table.field_names = ["nama warung", "rating", "status", "jam tutup"]
    for buku in data:
        status = get_status(buku[1]['jam buka'], buku[1]['jam tutup'], now)
        table.add_row([buku[0], buku[1]['rating'], status, buku[1]['jam tutup']])
    print(table)


