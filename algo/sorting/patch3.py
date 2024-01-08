import json
from prettytable import PrettyTable
import datetime


def selection_sort():
    with open("\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Tugas AKhir\\3\\data.json", "r") as f:
        dataa = json.load(f)

    data = list(dataa.items())
    now = datetime.datetime.now().time()
    n = len(data)
    a = 0
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if data[j][1]["rekomendasi"] > data[max_idx][1]["rekomendasi"]:
                max_idx = j
                data[i], data[max_idx] = data[max_idx], data[i]
                print(f"step ke-{a + 1} : {[buku[1]['rekomendasi'] for buku in data]}, iterasi ke-{i+1}")
                a += 1
        
    table = PrettyTable()
    table.field_names = ["Nama warung", "rating","jarak", "status", "jam buka", "jam tutup"]

    for info in data:
        jam_buka = datetime.datetime.strptime(info[1]['jam buka'], "%H:%M").time()
        jam_tutup = datetime.datetime.strptime(info[1]['jam tutup'], "%H:%M").time()
        if jam_buka <= now <= jam_tutup:
            status = "buka"
        else:
            status = "tutup"
        jrk = info[1]['jarak']
        if jrk > 1000:
            jarak = f"{jrk / 1000} KM"
        else:
            jarak = f"{jrk} M"
        table.add_row([info[0], info[1]["rating"], jarak, status, info[1]['jam buka'], info[1]["jam tutup"]])


    print(table)

