import json
from prettytable import PrettyTable
import datetime
import time

def selection_sort():
    global data
    global now
    with open("\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Tugas AKhir\\3\\data.json", "r") as f:
        dataa = json.load(f)

    data = list(dataa.items())
    now = datetime.datetime.now().time()
    n = len(data)
    a = 0
    waktuM = time.time()
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if data[j][1]["rekomendasi"] > data[max_idx][1]["rekomendasi"]:
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]
        print(f"step ke-{a + 1} : {[warung[1]['rekomendasi'] for warung in data]}, iterasi ke-{i+1}")
        a += 1
        if a == n - 1:
            break
    waktuS = time.time()
    waktuA = waktuS - waktuM
    print(f'Waktu : {waktuA:.6f}')

def coba1():
    global hasil
    global data
    selection_sort()
    result_list = []
    for warung in data:
        jam_buka = datetime.datetime.strptime(warung[1]['jam buka'], "%H:%M").time()
        jam_tutup = datetime.datetime.strptime(warung[1]['jam tutup'], "%H:%M").time()
        if jam_buka <= now <= jam_tutup:
            status = "buka"
        else:
            status = "tutup"
        result_list.append({
            "Nama warung": warung[0],
            "rekomendasi": warung[1]['rekomendasi'],
            "status": status,
            "jam buka": warung[1]['jam buka'],
            "jam tutup": warung[1]['jam tutup']
        })
        
    hasil = result_list

def selection_sort2():
    coba1()
    global data
    global now
    data = list(hasil)
    now = datetime.datetime.now().time()
    n = len(data)
    a = 0
    waktuM = time.time()
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if data[j]["status"] < data[max_idx]["status"]:
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]
        print(f"step ke-{a + 1} : {[warung['status'] for warung in data]}, iterasi ke-{i+1}")
        a += 1
        if a == n - 1:
            break
    waktuS = time.time()
    waktuA = waktuS - waktuM
    print(f'Waktu : {waktuA:.6f}')

def coba2():
    selection_sort2()
    table = PrettyTable()
    table.field_names = ["Nama warung", "rekomendasi", "status", "jam buka", "jam tutup"]
    for warung in data:
        table.add_row([warung["Nama warung"], warung['rekomendasi'], warung['status'], warung['jam buka'], warung['jam tutup']])
    print(table)

# Pangg
