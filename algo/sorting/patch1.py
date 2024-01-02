import json
import time
from prettytable import PrettyTable

with open("\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Tugas AKhir\\data.json", "r") as f:
    dataa = json.load(f)

rating = [buku["rating"] for buku in dataa.values()]
nama = [buku for buku in dataa.keys()]


data = list(dataa.items())

def insertion_sort(data):
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

    return data

sorted_data = insertion_sort(data)

print("\nWarung sebelum di sorting")
tabel = list(zip(nama, rating))

table1 = PrettyTable()
table1.field_names = ["nama warung", "rating"]
for buku in tabel:
    table1.add_row(buku)
print(table1)

print("\nWarung setelah di sorting by rating")

table = PrettyTable()
table.field_names = ["nama warung", "rating"]
for buku in sorted_data:
    table.add_row([buku[0], buku[1]['rating']])
print(table)

