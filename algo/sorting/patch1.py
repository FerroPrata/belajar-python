import json
import time
from prettytable import PrettyTable
import datetime



def warung_sorting():
    global array
    global now
    with open("D:/backup data 2023/optional/belajar python/algo/sorting/data.json", "r") as f:
        dataa = json.load(f)

    now = datetime.datetime.now().time()
    array = list(dataa.items())

    a = 0
    waktuM = time.time()
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j][1]["rating"] < key_item[1]["rating"]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
        print(f"step ke-{a + 1} : {[buku[1]['rating'] for buku in array]}, iterasi ke-{i}")
        a += 1

    waktuS = time.time()
    waktuA = waktuS - waktuM
    print(f'Waktu : {waktuA:.6f}')

def coba1():
    global array
    table = PrettyTable()
    table.field_names = ["Nama warung", "rating", "status", "jam tutup"]
    for buku in array:
        jam_buka = datetime.datetime.strptime(buku[1]['jam buka'], "%H:%M").time()
        jam_tutup = datetime.datetime.strptime(buku[1]['jam tutup'], "%H:%M").time()
        if jam_buka <= now <= jam_tutup:
            status = "buka"
        else:
            status = "tutup"
        table.add_row([buku[0], buku[1]['rating'], status, buku[1]['jam tutup']])
    print(table)

