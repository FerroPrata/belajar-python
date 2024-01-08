import json
from prettytable import PrettyTable
import datetime


def selection_sort():
    with open("\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Tugas AKhir\\2\\data.json", "r") as f:
        dataa = json.load(f)

    data = list(dataa.items())
    now = datetime.datetime.now().time()
    n = len(data)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if data[j][1]["rekomendasi"] > data[max_idx][1]["rekomendasi"]:
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]
        
    table = PrettyTable()
    table.field_names = ["Nama warung", "rekomendasi", "status", "jam buka", "jam tutup"]

    for info in data:
        jam_buka = datetime.datetime.strptime(info[1]['jam buka'], "%H:%M").time()
        jam_tutup = datetime.datetime.strptime(info[1]['jam tutup'], "%H:%M").time()
        if jam_buka <= now <= jam_tutup:
            status = "buka"
        else:
            status = "tutup"
        table.add_row([info[0],info[1]['rekomendasi'], status, info[1]['jam buka'], info[1]["jam tutup"]])

    print(table)

