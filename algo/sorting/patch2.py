import json
from prettytable import PrettyTable
import datetime
import time


def buble_sort():
    global array
    global now
    with open("D:/backup data 2023/optional/belajar python/algo/sorting/data.json", "r") as f:
        dataa = json.load(f)
    waktuM = time.time()
    data = list(dataa.items())
    now = datetime.datetime.now().time()
    a = 0
    array = data
    n = len(array) 
    for i in range(n):
        for j in range(n - i - 1): 
            if array[j][1]["jarak"] > array[j + 1][1]["jarak"]:                
                a += 1
                array[j], array[j + 1] = array[j + 1], array[j]
                bukun = [warung[1]['jarak'] for warung in data] 
                print(f"step ke {a} : {bukun}, iterasi ke {i + 1}")

    waktuS = time.time()
    waktuA = waktuS - waktuM
    print(f'Waktu : {waktuA:.6f}')

def coba():
    global array  
    table = PrettyTable()
    table.field_names = ["Nama warung", "jarak", "status", "jam buka", "jam tutup"]
    for warung in array:
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
        table.add_row([warung[0], jarak, status, warung[1]['jam buka'], warung[1]['jam tutup']])
        
    print(table)


