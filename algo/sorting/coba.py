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
        print(f"step ke-{a + 1} : {[warung[1]['rating'] for warung in array]}, iterasi ke-{i}")
        a += 1

    waktuS = time.time()
    waktuA = waktuS - waktuM
    print(f'Waktu : {waktuA:.6f}')

def coba1():
    global hasil
    global array
    warung_sorting()
    result_list = []
    for warung in array:
        jam_buka = datetime.datetime.strptime(warung[1]['jam buka'], "%H:%M").time()
        jam_tutup = datetime.datetime.strptime(warung[1]['jam tutup'], "%H:%M").time()
        if jam_buka <= now <= jam_tutup:
            status = "buka"
        else:
            status = "tutup"
        result_list.append({
            "Nama warung": warung[0],
            "rating": warung[1]['rating'],
            "status": status,
            "jam buka": warung[1]['jam buka'],
            "jam tutup": warung[1]['jam tutup']
        })

    hasil = result_list

def warung_sorting2():
    coba1()
    global array
    global now

    now = datetime.datetime.now().time()
    array = list(hasil)

    a = 0
    waktuM = time.time()
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j]["status"] > key_item["status"]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
        print(f"step ke-{a + 1} : {[warung['status'] for warung in array]}, iterasi ke-{i}")
        a += 1

    waktuS = time.time()
    waktuA = waktuS - waktuM
    print(f'Waktu : {waktuA:.6f}')



def coba2():
    warung_sorting2()
    table = PrettyTable()
    table.field_names = ["Nama warung", "rating", "status", "jam buka", "jam tutup"]
    for warung in array:
        table.add_row([warung["Nama warung"], warung['rating'], warung['status'], warung['jam buka'], warung['jam tutup']])
    print(table)

coba2()