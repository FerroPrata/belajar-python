import json
from prettytable import PrettyTable
import datetime


def selection_sort():
    global data
    global now
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
                print(f"step ke-{a + 1} : {[warung[1]['rekomendasi'] for warung in data]}, iterasi ke-{i+1}")
                a += 1
def helo():  
    global data
    global now 
    table = PrettyTable()
    table.field_names = ["Nama warung", "rekomendasi", "rating","jarak", "status", "jam buka", "jam tutup"]

    for warung in data:
        jam_buka = datetime.datetime.strptime(warung[1]['jam buka'], "%H:%M").time()
        jam_tutup = datetime.datetime.strptime(warung[1]['jam tutup'], "%H:%M").time()
        if jam_buka <= now <= jam_tutup:
            status = "buka"
        else:
            status = "tutup"
        jrk = warung[1]['jarak']
        if jrk > 1000:
            jarak = f"{jrk / 1000} KM"
        else:
            jarak = f"{jrk} M"
        table.add_row([warung[0], "{:.1f}".format(warung[1]['rekomendasi']), warung[1]["rating"], jarak, status, warung[1]['jam buka'], warung[1]["jam tutup"]])



    print(table)