import json
import time
from prettytable import PrettyTable

with open("D:/backup data 2023/optional/belajar python/algo/sorting/data.json", "r") as f:
    dataa = json.load(f)

tahun_terbit_list = [buku["tahun_terbit"] for buku in dataa.values()]
nama = [buku for buku in dataa.keys()]


data = list(dataa.items())

def insertion_sort(data):
    a = 0
    waktuM = time.time()
    for i in range(1, len(data)):  
        key_item = data[i]  
        j = i - 1  
        while j >= 0 and data[j][1]["tahun_terbit"] > key_item[1]["tahun_terbit"]:  
            data[j + 1] = data[j]  
            j -= 1
        data[j + 1] = key_item  
        print(f"step ke-{a} : {[buku[1]['tahun_terbit'] for buku in data]}, iterasi ke-{i}")
        a += 1

    waktuS = time.time()
    waktuA = waktuS - waktuM
    print(f'Waktu : {waktuA:.6f}')

    return data

sorted_data = insertion_sort(data)

print("\nbuku sebelum di sorting")
tabel = list(zip(nama, tahun_terbit_list))

table1 = PrettyTable()
table1.field_names = ["nama buku", "tahun terbit"]
for buku in tabel:
    table1.add_row(buku)
print(table1)

print("\nbuku setelah di sorting by tahun")

table = PrettyTable()
table.field_names = ["nama buku", "tahun terbit"]
for buku in sorted_data:
    table.add_row([buku[0], buku[1]['tahun_terbit']])
print(table)

